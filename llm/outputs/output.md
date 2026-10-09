S1 [interpretation] **Cluster 1 may represent vascular/aortic biomechanics and pathology**, focusing on arterial structures and hemodynamic/mechanical context (cluster 1: aortic, vascular, wall, artery, muscle, aorta, smooth, arterial, aneurysm, vessel, pressure, blood, diameter).

S2 [interpretation] **Cluster 2 may represent elastin-related biomaterials/chemistry and translational use concepts**, including polymers/polypeptides, sequences, and application/drug framing (cluster 2: peptide, material, acid, system, application, new, sequence, temperature, potential, polymer, polypeptide, drug).

S3 [interpretation] **Cluster 3 may represent skin/dermal tissue engineering and cell culture work around elastin production**, including scaffolds, fibroblasts, and in vitro/in vivo contexts (cluster 3: skin, scaffold, fibroblast, vitro, tropoelastin, vivo, culture, production, graft, synthesis, proliferation, dermal, endothelial).

S4 [interpretation] **Cluster 4 may represent core extracellular matrix (ECM) and tissue composition framing**, centered on elastin/collagen/cells/tissue/matrix and related descriptors (cluster 4: elastin, cell, collagen, tissue, protein, matrix, human, extracellular, component).

S5 [interpretation] **Cluster 5 may represent molecular/clinical biology of elastin in disease**, emphasizing expression/gene regulation, enzymes (including elastase), inhibitors, and pulmonary/lung disease context (cluster 5: expression, patient, lung, level, activity, disease, gene, role, factor, development, formation, growth, elastase, process, mechanism, clinical, degradation, pulmonary, enzyme, molecular, important, inhibitor, interaction, case, syndrome).

S6 [interpretation] **Cluster 6 may represent experimental study design and in vivo model-based intervention/effects**, with animal models, treatment, time-course, and comparative language (cluster 6: group, mouse, effect, model, change, control, treatment, rat, day, increase, significant, content, response, age, higher, difference, week, animal, lower).

S7 [interpretation] **Cluster 7 may represent mechanical/structural characterization of elastic fibers and tissues**, including mechanical properties, stiffness, and structure/function descriptors (cluster 7: fiber, elastic, property, structure, type, mechanical, different, function, normal, high, structural, similar, surface, time, concentration, sample, layer, region, area, stress, condition, valve, microscopy, stiffness, presence, strain, specific, membrane, number).

S8 [data] **The co-occurrence network contains a large mixed subgraph combining Cluster 4 (core ECM terms) with Cluster 7 (fiber/elastic) and Cluster 6 (“effect”)**, suggesting these vocabularies frequently appear together (subgraph 2: elastin, cell, collagen, tissue, protein, matrix, component, extracellular, human, fiber, elastic, effect).

S9 [interpretation] **Core ECM/tissue composition (Cluster 4) and mechanical/elastic-fiber framing (Cluster 7) appear tightly coupled as a broader domain**, because Cluster 7 terms (fiber, elastic) sit in the same subgraph as Cluster 4 terms and have direct edges to them (subgraph 2; edges: collagen–fiber, tissue–fiber, tissue–elastic, fiber–elastic; clusters 4↔7).

S10 [interpretation] **Vascular/aortic research (Cluster 1) is connected to the core ECM/cell domain (Cluster 4) via “cell” links to vascular muscle/smooth terms**, implying overlap between vascular wall biology and general ECM/cell discussions (edge between subgraphs: cell–muscle; cell–smooth; clusters 4↔1; subgraphs 2↔1).

S11 [data] **Cluster 1 forms a coherent vascular subgraph with dense internal co-occurrence**, indicating a relatively self-contained vocabulary around arteries/aorta and related terms (subgraph 1: wall, artery, muscle, aorta, aneurysm, vessel, blood, pressure, aortic, vascular, smooth, arterial).

S12 [data] **Gene/expression terms form their own subgraph and connect outward to core ECM terms**, indicating that expression language co-occurs with cell/protein/matrix language (subgraph 7: expression, level, gene; edges: cell–expression, protein–expression, matrix–expression; clusters 5↔4; subgraphs 7↔2).

S13 [interpretation] **This pattern suggests a broader “ECM biology and regulation” domain combining Cluster 4 (ECM components) with parts of Cluster 5 (expression/gene)**, because the expression subgraph is directly bridged to the ECM subgraph by multiple edges (edges: cell–expression, protein–expression, matrix–expression; clusters 4↔5; subgraphs 2↔7).

S14 [data] **Some Cluster 5 content is compartmentalized into smaller, internally linked subgraphs**, including enzyme/activity, lung/pulmonary, and factor/growth (subgraph 4: activity–enzyme; subgraph 10: lung–pulmonary; subgraph 9: factor–growth).

S15 [data] **Cluster 3 splits across multiple subgraphs, with a skin/dermal/fibroblast subgraph and a vitro/vivo subgraph**, while several Cluster 3 terms have no network edges retained (subgraph 5: skin, dermal, fibroblast; subgraph 8: vitro, vivo; cluster 3 terms without edges include scaffold, tropoelastin, culture, graft, synthesis).

S16 [interpretation] **The separation of “skin/dermal/fibroblast” from “vitro/vivo” suggests at least two partially distinct emphases within Cluster 3** (dermal cell context vs experimental setting language), rather than one single tightly connected topic in the strongest co-occurrences (subgraphs 5 and 8: skin/dermal/fibroblast vs vitro/vivo).

S17 [data] **Cluster 2 is weakly represented in the network, appearing mainly as a small temperature–polypeptide subgraph**, with many Cluster 2 terms lacking retained edges (subgraph 3: temperature, polypeptide; cluster 2 terms without edges include material, polymer, drug, application, sequence).

S18 [interpretation] **This may indicate that Cluster 2’s “materials/application/drug” vocabulary is more diffuse across abstracts or co-occurs with many different contexts rather than forming one dominant co-occurrence core** (cluster 2 vs limited subgraph 3 presence: temperature, polypeptide).

S19 [data] **Cluster 7’s mechanical-property vocabulary appears as a small dedicated subgraph (property–mechanical) and also links into the core ECM subgraph via fiber/elastic**, indicating both a specialized and an integrated role (subgraph 11: property, mechanical; subgraph 2: fiber, elastic; edge: fiber–elastic; clusters 7↔7 and 7↔4).

S20 [data] **In the correspondence analysis output, “collagen,” “fiber,” and “human” are explicitly labeled as not characteristic of any period**, implying relative stability across time slices in this analysis (not characteristic: collagen, fiber, human).

S21 [data] **The period 1975–1979 is characterized by chemistry/biochemistry and basic composition/structure terms plus aorta**, including acid, synthesis, membrane, content, age, and aorta (period 1975–1979: acid, synthesis, aorta, membrane, content, age).

S22 [interpretation] **This early-period profile may reflect foundational work emphasizing biochemical composition/formation and basic tissue/organ context rather than later translational or engineering framing** (period 1975–1979: acid, synthesis, membrane, content, age, aorta).

S23 [data] **The period 1980–1989 is characterized by enzyme-related terms (including elastase) plus animal and elastin, alongside synthesis/membrane/content/age**, indicating a shift toward enzymatic processes and model organisms in the characteristic vocabulary (period 1980–1989: elastase, enzyme, synthesis, membrane, animal, elastin, content, age).

S24 [interpretation] **Compared with 1975–1979, the appearance of elastase/enzyme/animal among characteristic terms suggests increased emphasis on enzymatic degradation/processing and animal-based study contexts** (periods 1975–1979 vs 1980–1989: elastase, enzyme, animal newly characteristic in 1980–1989).

S25 [data] **The period 1990–1999 is characterized by tropoelastin, rat, pulmonary, muscle, and terms implying detection/comparison/change (presence, increase, similar, component)** (period 1990–1999: tropoelastin, rat, presence, increase, similar, component, pulmonary, muscle).

S26 [interpretation] **This profile may indicate a stronger focus on elastin precursor biology (tropoelastin) and organ/physiology-linked contexts (pulmonary, muscle) in animal studies** (period 1990–1999: tropoelastin, rat, pulmonary, muscle).

S27 [data] **The period 2000–2009 is characterized by sequence and syndrome alongside vascular-structure terms (wall, artery) and spatial/typing terms (region, type)** (period 2000–2009: sequence, syndrome, region, wall, type, artery).

S28 [interpretation] **This combination may indicate increased attention to genotype/sequence-linked conditions (sequence, syndrome) together with vascular wall/artery framing** (period 2000–2009: sequence, syndrome, wall, artery).

S29 [data] **The period 2010–2019 is characterized by scaffold and mechanical/function terms plus vascular and clinical framing, with mouse as the characteristic model term** (period 2010–2019: scaffold, mouse, clinical, vascular, mechanical, function).

S30 [interpretation] **This pattern may indicate growth of tissue engineering/regenerative approaches (scaffold) and biomechanics (mechanical/function) with more explicit clinical/vascular positioning** (period 2010–2019: scaffold, mechanical, function, clinical, vascular).

S31 [data] **The period 2020–2025 is characterized by application-oriented and translational terms (application, drug, treatment, potential) plus material/property and skin/polypeptide** (period 2020–2025: application, drug, potential, treatment, material, property, skin, polypeptide).

S32 [interpretation] **Relative to earlier periods, the characteristic vocabulary in 2020–2025 suggests a stronger translational/technology framing (application/drug/treatment/potential) alongside materials and measurable properties** (period 2020–2025: application, drug, treatment, potential, material, property).

S33 [interpretation] **Across periods, the characteristic terms suggest a trajectory from basic biochemical descriptors (acid/synthesis/membrane/content) toward enzymes/animal models, then precursor/organ contexts, then sequence/syndrome with vascular structure, and finally scaffold/mechanics and application/drug/material emphases** (period blocks 1975–1979; 1980–1989; 1990–1999; 2000–2009; 2010–2019; 2020–2025: listed characteristic terms).

S34 [interpretation] **Overall, the term clusters suggest multiple coexisting domains—vascular wall/aorta (Cluster 1), core ECM composition (Cluster 4), mechanical properties (Cluster 7), molecular regulation/disease (Cluster 5), experimental model/effects language (Cluster 6), dermal/skin tissue engineering (Cluster 3), and materials/application concepts (Cluster 2)** (S1–S7).

S35 [interpretation] **The co-occurrence network implies that ECM composition and elastic/mechanical framing form a central integrative hub, with bridges to gene/expression biology and to vascular wall topics** (S8–S13, S19).

S36 [interpretation] **The period analysis suggests that, while some core terms remain non-characteristic (stable), the field’s distinctive emphases shift over time toward engineering/mechanics and translational application language in the most recent periods** (S20–S33).