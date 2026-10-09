"""Figure 1: the KH Coder dendrogram redrawn in two columns from the tree extracted by dendro_extract.py.

Usage: python make_figure1.py dendro.json out_basename
Panels: (A) Clusters 1-4, (B) Clusters 5-7 (within-cluster merges, below the cut), (C) merging of the
seven clusters above the cut. Heights, leaf order, frequencies and cluster colors are those of the KH Coder output.
"""
import json, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

d = json.load(open(sys.argv[1]))
out = sys.argv[2]
leaves = d['leaves']; nodes = {n['id']: n for n in d['nodes']}; cut = d['cut']
order = [l['term'] for l in leaves]
info = {l['term']: l for l in leaves}
ypos = {t: i for i, t in enumerate(order)}            # 0 = top
colors = {}
for l in leaves:
    colors.setdefault(l['cluster'], tuple(l['color']))
GRAY = (0.45, 0.45, 0.45)
FONT = 7


def node_leaves(nid):
    out = []
    for kind, c in nodes[nid]['children']:
        out.extend(node_leaves(c) if kind == 'node' else [c])
    return out


def node_y(nid):
    ys = []
    for kind, c in nodes[nid]['children']:
        ys.append(node_y(c) if kind == 'node' else ypos[c])
    return sum(ys) / len(ys)


def draw_tree(ax, nid, lw=0.8):
    """Draw the subtree rooted at nid; returns (x, y) of its root junction."""
    n = nodes[nid]
    ls = node_leaves(nid)
    cl = {info[t]['cluster'] for t in ls}
    col = colors[next(iter(cl))] if len(cl) == 1 else GRAY
    h = n['height']; ys = []
    for kind, c in n['children']:
        if kind == 'node':
            cx, cy = draw_tree(ax, c, lw)
        else:
            cx, cy = 0.0, ypos[c]
        ax.plot([cx, h], [cy, cy], color=col, lw=lw, solid_capstyle='butt')
        ys.append(cy)
    ax.plot([h, h], [min(ys), max(ys)], color=col, lw=lw, solid_capstyle='butt')
    return h, sum(ys) / len(ys)


def cluster_roots(clusters):
    """ids of the highest nodes whose leaves all belong to one of the given clusters (one per cluster)."""
    roots = {}
    for nid, n in nodes.items():
        ls = node_leaves(nid)
        cl = {info[t]['cluster'] for t in ls}
        if len(cl) == 1 and n['height'] < cut:
            c = next(iter(cl))
            if c in clusters and (c not in roots or n['height'] > nodes[roots[c]]['height']):
                roots[c] = nid
    return roots


MAXF = max(l['freq'] for l in leaves)


def dendro_panel(ax, clusters, label):
    roots = cluster_roots(clusters)
    terms = [t for t in order if info[t]['cluster'] in clusters]
    y0, y1 = ypos[terms[0]], ypos[terms[-1]]
    for c, nid in roots.items():
        hx, hy = draw_tree(ax, nid)
        # stub to the cut line and the cluster number
        ax.plot([hx, cut], [hy, hy], color=GRAY, lw=0.8, ls=(0, (2, 2)))
        ax.text(cut + 0.02, hy, 'Cluster %d' % c, fontsize=FONT, va='center', ha='left', color=colors[c], fontweight='bold')
    # labels and frequency bars
    BARW = 0.26  # width of the bar area in dissimilarity units
    for t in terms:
        y = ypos[t]; c = info[t]['cluster']
        ax.text(-0.03, y, t, fontsize=FONT, va='center', ha='right', color=colors[c])
        w = BARW * info[t]['freq'] / MAXF
        ax.barh(y, w, left=-0.50 - w, height=0.7, color=colors[c], alpha=0.55, lw=0)
    ax.axvline(cut, color='black', lw=0.8, ls=(0, (4, 3)))
    ax.set_xlim(-0.80, 1.72)
    ax.set_ylim(y1 + 0.8, y0 - 0.8)
    ax.set_xticks([0, 0.5, 1.0])
    ax.set_xticklabels(['0', '0.5', '1.0'], fontsize=FONT)
    ax.set_yticks([])
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_bounds(0, 1.3)
    ax.spines['bottom'].set_linewidth(0.6)
    ax.tick_params(axis='x', length=2, width=0.6, pad=2)
    ax.set_xlabel('Dissimilarity', fontsize=FONT, labelpad=2)
    ax.xaxis.set_label_coords(0.62, -0.012 if len(terms) > 60 else -0.02)


def cluster_panel(ax, label):
    # cluster-level tree: leaves are the seven clusters in dendrogram order
    roots = cluster_roots(range(1, 8))
    cl_order = []
    for t in order:
        c = info[t]['cluster']
        if c not in cl_order:
            cl_order.append(c)
    cy = {c: i for i, c in enumerate(cl_order)}
    sizes = {c: sum(1 for t in order if info[t]['cluster'] == c) for c in cl_order}
    top3 = {c: [t for t in sorted((t for t in order if info[t]['cluster'] == c), key=lambda t: -info[t]['freq'])][:3] for c in cl_order}

    def draw(nid):
        n = nodes[nid]
        ls = node_leaves(nid)
        cl = {info[t]['cluster'] for t in ls}
        if len(cl) == 1:  # a whole cluster: leaf of this panel
            c = next(iter(cl))
            return cut, cy[c]
        h = n['height']; ys = []
        for kind, c in n['children']:
            cx, yy = draw(c)
            ax.plot([cx, h], [yy, yy], color=GRAY, lw=0.9)
            ys.append(yy)
        ax.plot([h, h], [min(ys), max(ys)], color=GRAY, lw=0.9)
        ax.text(h, min(ys) - 0.12, '%.2f' % h, fontsize=FONT - 1, ha='center', va='bottom', color=GRAY)
        return h, sum(ys) / len(ys)

    draw(d['root'])
    for c in cl_order:
        ax.text(cut - 0.015, cy[c], 'Cluster %d (%d terms)' % (c, sizes[c]),
                fontsize=FONT, va='center', ha='right', color=colors[c], fontweight='bold')
    ax.axvline(cut, color='black', lw=0.8, ls=(0, (4, 3)))
    ax.set_xlim(0.88, 1.72)
    ax.set_ylim(len(cl_order) - 0.4, -0.9)
    ax.set_xticks([1.3, 1.4, 1.5, 1.6])
    ax.set_xticklabels(['1.3', '1.4', '1.5', '1.6'], fontsize=FONT)
    ax.set_yticks([])
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_bounds(cut, 1.7)
    ax.spines['bottom'].set_linewidth(0.6)
    ax.tick_params(axis='x', length=2, width=0.6, pad=2)
    ax.set_xlabel('Dissimilarity', fontsize=FONT, labelpad=2)
    ax.xaxis.set_label_coords(0.72, -0.06)


plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['pdf.fonttype'] = 42
nA = sum(1 for t in order if info[t]['cluster'] <= 4)
nB = len(order) - nA
H = 9.6; W = 7.3
fig = plt.figure(figsize=(W, H))
top, bottom = 0.975, 0.03
rowh = (top - bottom) / (nB + 2.0)          # height per leaf row (right column)
hA = rowh * (nA + 2.0); hB = rowh * (nB + 2.0)
axA = fig.add_axes([0.02, top - hA, 0.47, hA])
axB = fig.add_axes([0.52, top - hB, 0.47, hB])
axC = fig.add_axes([0.02, bottom + 0.012, 0.47, top - hA - bottom - 0.07])
dendro_panel(axA, {1, 2, 3, 4}, '(A)')
dendro_panel(axB, {5, 6, 7}, '(B)')
cluster_panel(axC, '(C)')
fig.text(0.02, 0.985, '(A)', fontsize=9, fontweight='bold', va='center', ha='left')
fig.text(0.52, 0.985, '(B)', fontsize=9, fontweight='bold', va='center', ha='left')
fig.text(0.02, top - hA - 0.045, '(C)', fontsize=9, fontweight='bold', va='center', ha='left')
fig.savefig(out + '.pdf')
fig.savefig(out + '.png', dpi=300)
print('saved', out)
