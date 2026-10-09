"""Extract the dendrogram (leaf order, labels, label colors, merge heights, cut level) from the
PDF saved by KH Coder's hierarchical cluster analysis, and write it as JSON.

Usage: python dendro_extract.py Figure_1.pdf terms.json out.json
  terms.json: {"term": {"freq": int, "cluster": int, ...}, ...}  (used to attach frequencies)
Requires pdfplumber.
"""
import collections, json, sys
import pdfplumber

pdf_path, terms_path, out_path = sys.argv[1:4]
terms = json.load(open(terms_path, encoding='utf-8'))
pg = pdfplumber.open(pdf_path).pages[0]


def undouble(s):  # KH Coder draws bold labels twice; pdfplumber returns doubled characters
    return s[0::2] if len(s) % 2 == 0 and s[0::2] == s[1::2] else s


words = pg.extract_words(extra_attrs=['non_stroking_color'])
labels = {}
for w in words:
    t = undouble(w['text'])
    if t in terms:
        col = w.get('non_stroking_color')
        labels[t] = {'x1': w['x1'], 'y': (w['top'] + w['bottom']) / 2, 'color': list(col) if col else None}
assert len(labels) == len(terms), (len(labels), len(terms))

# axis scale from the tick labels 0.0 / 0.5 / 1.0
ticks = {undouble(w['text']): (w['x0'] + w['x1']) / 2 for w in words if undouble(w['text']) in ('0.0', '0.5', '1.0')}
X0 = ticks['0.0']; SCALE = (ticks['1.0'] - ticks['0.0'])
d = lambda x: (x - X0) / SCALE

lines = pg.lines
vs = [(l['x0'], l['top'], l['bottom']) for l in lines if abs(l['x0'] - l['x1']) < 0.01]
hs = [(min(l['x0'], l['x1']), max(l['x0'], l['x1']), l['top']) for l in lines if abs(l['top'] - l['bottom']) < 0.01]
# full-height verticals: grid lines at multiples of 0.25 and the dashed cut line
longv = sorted({round(d(x), 3) for x, t, b in vs if b - t > 2000})
cut = [v for v in longv if abs(v * 4 - round(v * 4)) > 0.01]
assert len(cut) == 1, longv
cut = cut[0]


def merge_segments(segs, key_idx, lo_idx, hi_idx):
    by = collections.defaultdict(list)
    for s in segs:
        by[round(s[key_idx], 2)].append((s[lo_idx], s[hi_idx]))
    out = []
    for k, ss in by.items():
        ss.sort()
        cur = list(ss[0])
        for lo, hi in ss[1:]:
            if abs(lo - cur[1]) < 0.05:
                cur[1] = hi
            else:
                out.append((k, cur[0], cur[1])); cur = [lo, hi]
        out.append((k, cur[0], cur[1]))
    return out


dv = merge_segments([(x, t, b) for x, t, b in vs if b - t <= 2000 and x > X0 + 0.5], 0, 1, 2)
dh = merge_segments(hs, 2, 0, 1)  # (y, xa, xb)
nodes = [{'id': i, 'x': x, 'y0': t, 'y1': b, 'ym': (t + b) / 2, 'h': d(x)} for i, (x, t, b) in enumerate(dv)]


def has_h(xa, xb, y):
    return any(abs(a - xa) < 1.5 and abs(b - xb) < 1.5 and abs(yy - y) < 2.5 for yy, a, b in dh)


def find_child(x, y):
    for n in sorted(nodes, key=lambda n: -n['x']):
        if n['x'] < x - 0.01 and abs(n['ym'] - y) < 2.5 and has_h(n['x'], x, n['ym']):
            return ['node', n['id']]
    for name, lab in labels.items():
        if abs(lab['y'] - y) < 3.5 and has_h(X0, x, lab['y']):
            return ['leaf', name]
    raise SystemExit('unresolved child at x=%.2f y=%.2f' % (x, y))


for n in nodes:
    n['children'] = [find_child(n['x'], n['y0']), find_child(n['x'], n['y1'])]
root = max(nodes, key=lambda n: n['x'])
byid = {n['id']: n for n in nodes}


def leaves(n):
    out = []
    for kind, c in n['children']:
        out.extend(leaves(byid[c]) if kind == 'node' else [c])
    return out


order = leaves(root)
assert len(order) == len(terms) == len(set(order))
leaf_order = sorted(labels, key=lambda t: labels[t]['y'])  # top to bottom as drawn
assert leaf_order == order, 'leaf order from the tree differs from the drawn order'
out = {
    'cut': cut,
    'leaves': [{'term': t, 'freq': terms[t]['freq'], 'cluster': terms[t]['cluster'], 'color': labels[t]['color']} for t in order],
    'nodes': [{'id': n['id'], 'height': round(n['h'], 4), 'children': n['children']} for n in nodes],
    'root': root['id'],
}
json.dump(out, open(out_path, 'w'), indent=1)
print('leaves', len(order), 'merges', len(nodes), 'cut', cut, 'root height', round(root['h'], 4))
