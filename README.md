# From matrix to materials: Mapping five decades of elastin research through multivariate text mining

Data and code for the manuscript *From matrix to materials: Mapping five decades of elastin research through multivariate text mining* (Y. Kobayashi, Y. Kusunoki, I. Kageyama, H. Wachi, K. Kodama; submitted to *International Journal of Biological Macromolecules*, 2026).

The study maps the vocabulary of elastin research in 20,217 Web of Science records (1975–2025) with KH Coder: frequent-term analysis, hierarchical cluster analysis, co-occurrence network analysis and correspondence analysis by publication period, with a large language model used only as an aid to interpretation.

The bibliographic records and abstracts retrieved from the Web of Science cannot be redistributed under the terms of the database provider and are **not** included. Everything derived from them that the manuscript reports is here.

## Contents

| Path | Description |
|---|---|
| `data/stopwords.txt` | The 175-entry stop-word list applied in KH Coder (one entry per line; matched against Stanford POS Tagger lemmas). Grouped by category in `tables/Table_S3.xlsx`. |
| `data/wordlist_nouns_adjectives.csv` | All nouns and adjectives extracted from the 19,125 abstracts after the stop-word list, with frequencies (KH Coder word list, exported 8 October 2026). |
| `data/terms120.csv` | The 120 most frequent nouns and adjectives (minimum frequency 1,836) with part of speech, frequency, rank, cluster (1–7), subgraph in the co-occurrence network (Figure 2) and use in the correspondence analysis (Figure 3). |
| `data/clusters_khcoder_export.xlsx` | Cluster membership as exported from KH Coder (seven clusters; Japanese column headers "クラスター1" … "クラスター7"). |
| `data/dendrogram_tree.json` | Leaf order, label colors, merge heights and cut level of the dendrogram, read from the PDF saved by KH Coder (`figures/Figure_S2.pdf`) with `scripts/dendro_extract.py`. |
| `data/cooccurrence_network_khcoder.html` | The co-occurrence network as exported by KH Coder (interactive HTML; 44 terms, 60 edges, 11 subgraphs). |
| `data/network_nodes.csv`, `data/network_edges.csv` | The same network as tables (term, subgraph, frequency; source, target, within-subgraph flag). |
| `data/ca_characteristic_terms_monkin_ja.txt` | Characteristic terms of each period as output by Monkin Reporting for KH Coder (Japanese, unedited). |
| `data/ca_terms_figure3.csv`, `data/ca_periods_figure3.csv` | Coordinates of the 60 terms and the six periods on the first two dimensions, read from the PDF of Figure 3, with distance and angle from the origin and the sector(s) as drawn. |
| `data/period_counts.csv` | Numbers of records and of records with an abstract per period (Table S2). |
| `figures/` | Figures 1–3 and Figures S1–S2 of the manuscript (vector PDF, fonts embedded). |
| `tables/` | Supplementary Tables S1–S3. |
| `scripts/` | `dendro_extract.py` (PDF → `dendrogram_tree.json`) and `make_figure1.py` (`dendrogram_tree.json` → Figure 1). |
| `llm/` | Code, prompts, inputs and outputs of the LLM-assisted interpretation (see `llm/README.md`). |

## How the data were produced

**Search.** Web of Science, All Databases, topic search `TS=(elastin OR tropoelastin OR "elastic fiber") AND PY=(1975-2025)`, run on 10 March 2026; 20,217 records, of which 19,125 (94.6%) had an abstract. Only abstracts were analyzed.

**Preprocessing (KH Coder 3.02c).** Stanford POS Tagger for lemmatization and tagging; each abstract (one spreadsheet cell, KH Coder unit "H5") treated as one document; the stop-word list in `data/stopwords.txt` applied as "words to exclude" (使用しない語) before preprocessing.

**Term selection.** Nouns and adjectives ranked by total frequency; the top 120 terms (95 nouns, 25 adjectives; minimum frequency 1,836) used in all three multivariate analyses. In the KH Coder dialogs: part of speech = Noun and Adj, minimum term frequency = 1836 (gives 120 terms).

**Hierarchical cluster analysis.** Jaccard distance, Ward's method, unit H5. The number of clusters (seven) was chosen with reference to the candidates marked by Monkin Reporting for KH Coder (version 2.0; SCREEN Advanced System Solutions) on the agglomeration plot (`figures/Figure_S1.pdf`); see Section 2.6 of the manuscript for the rationale.

**Co-occurrence network.** Jaccard coefficient, the 60 strongest edges (KH Coder default), subgraph detection by the modularity-based method (KH Coder default), node size proportional to frequency.

**Correspondence analysis.** Terms × publication period (six periods as an external variable), the 60 terms with the largest chi-square values (KH Coder default), first two dimensions (84.26% and 10.09% of the inertia). The sectors and the dashed circle in Figure 3 were drawn by Monkin Reporting for KH Coder.

**Figure 1.** Redrawn in two columns from the KH Coder dendrogram:

```
pip install -r scripts/requirements.txt
python scripts/dendro_extract.py figures/Figure_S2.pdf data/terms120.json data/dendrogram_tree.json   # optional: regenerate the tree
python scripts/make_figure1.py data/dendrogram_tree.json Figure_1
```

(`dendro_extract.py` expects the term list as JSON with `freq` and `cluster` per term; the tree it produces is already provided as `data/dendrogram_tree.json`, so the second command alone reproduces Figure 1.) Versions used: Python 3.13.16, Matplotlib 3.11.2, pdfplumber 0.11.10.

**LLM-assisted interpretation.** See `llm/`.

## Citation

Please cite the manuscript (see `CITATION.cff`). The repository is archived on Zenodo; the DOI is given in the manuscript's Data availability statement.

## License

Code: MIT (see `LICENSE`). Data tables and figures: Creative Commons Attribution 4.0 (CC BY 4.0). KH Coder and Monkin Reporting for KH Coder are separate software by their respective authors.
