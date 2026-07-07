# PRISMA-ScR-Spatio-Temporal-GNN
PRISMA-ScR search strategy and reproducible pipeline for Spatio-Temporal Graph Neural Networks across sensor-driven urban and environmental applications

### Repo structure
```
PRISMA-ScR-Spatio-Temporal-GNN/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── .gitignore
│
├── 01_search_strategy/
│   ├── concepts.yaml
│   ├── databases.yaml
│   ├── generated_queries/
│   │   ├── acm.txt
│   │   ├── arxiv.txt
│   │   ├── scopus.txt
│   │   ├── ieee_xplore.txt
│   │   ├── sciencedirect.txt
│   │   ├── web_of_science.txt
│   │   └── all_queries.csv
│   ├── generator.py
│   └── README.md
│
├── 02_retrieved_literature/
│   ├── raw_exports/
│   │   ├── scopus.bib
│   │   ├── ieee.ris
│   │   ├── wos.csv
│   │   └── arxiv.json
│   │
│   ├── deduplicated/
│   │   ├── master_library.bib
│   │   └── master_library.csv
│   │
│   ├── screening/
│   │   ├── title_abstract_screening.xlsx
│   │   ├── full_text_screening.xlsx
│   │   └── prisma_flow_data.csv
│   │
│   └── included_studies.csv
│
├── 03_paper_collection/
│   ├── README.md
│   │
│   ├── traffic_forecasting/
│   │   ├── STGCN/
│   │   │   ├── paper.pdf
│   │   │   ├── citation.bib
│   │   │   ├── code_link.txt
│   │   │   └── notes.md
│   │   │
│   │   ├── GraphWaveNet/
│   │   │   ├── ...
│   │   │
│   │   └── ...
│   │
│   ├── trajectory_prediction/
│   │   ├── SocialSTGCN/
│   │   ├── AgentFormer/
│   │   └── ...
│   │
│   └── environmental_modeling/
│       ├── DCRNN/
│       ├── MTGNN/
│       └── ...
│
├── 04_code_models/
│   ├── README.md
│   ├── baselines/
│   ├── preprocessing/
│   ├── evaluation/
│   └── utilities/
│
├── 05_analysis/
│   ├── notebooks/
│   │   ├── taxonomy_analysis.ipynb
│   │   ├── temporal_model_comparison.ipynb
│   │   └── application_comparison.ipynb
│   │
│   ├── figures/
│   ├── tables/
│   └── results.csv
│
└── 06_prisma_reporting/
    ├── prisma_diagram.png
    ├── prisma_data.xlsx
    ├── inclusion_exclusion_rules.md
    └── search_strategy_appendix.md
```
