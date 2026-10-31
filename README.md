# Principled Unified Spatio-Temporal Graph Neural Networks for Traffic Forecasting: A Scoping Review

Official open-science repository for the systematic scoping review: **"Principled Unified Spatio-Temporal Graph Neural Networks for Traffic Forecasting: A Scoping Review"** by Clayton K. Baker and Clement N. Nyirenda (Department of Computer Science, University of the Western Cape).

---

## 📌 Repository Contents

```text
.
├── 01_search_strategy/
│   ├── concepts.yaml
│   ├── databases.yaml
│   ├── search_generator.py
│   └── generated_queries/
│       ├── acm_digital_library.txt
│       ├── ieee_xplore.txt
│       ├── scopus.txt
│       └── all_searches.csv
├── 02_retrieved_literature/
│   ├── acm_digital_library.bib
│   ├── ieee_xplore.bib
│   └── scopus.bib
├── 03_results_tables/
│   ├── Table3.tex
│   ├── Table4.tex
│   ├── Table5.tex
│   ├── Table6.tex
│   └── Table7.tex
├── Master_ScR_data_extraction.xlsx
└── PRISMA_ScR_checklist.pdf
```
---

## 📚 Indexed Collection of Primary Included Studies (N = 28)

Below is the complete indexed catalog of the 28 primary studies (2025–2026) evaluated in this scoping review, including paper DOIs, target venues, and open-source code repository links.

| ID | Model | Year | Paper Title & DOI Link | Target Venue | Code Repository & Accessibility |
| :---: | :--- | :---: | :--- | :--- | :--- |
| 1 | **AST-SGCN** | 2025 | Attention-based spatial-temporal synchronous graph convolution networks for traffic flow forecasting (https://doi.org/10.1007/s10489-025-06341-4) | *Applied Intelligence* | private (on request) |
| 2 | **ASTEGCN** | 2025 | ASTE: adaptive spatial-temporal enhanced graph convolution network for traffic flow prediction (https://doi.org/10.1007/s10586-025-05559-8) | *Cluster Computing* | not reported |
| 3 | **ASTMGODE** | 2025 | Attention based spatial-temporal multi-graph ordinary differential equation network for traffic flow prediction (https://doi.org/10.1016/j.engappai.2025.110526) | *Engineering Applications of Artificial Intelligence* | not reported |
| 4 | **C-ChebNet** | 2025 | ChebNet Traffic Flow Prediction Model Based on Non-local Spatio-temporal Correlation Matrix (https://doi.org/10.1007/s11067-025-09688-w) | *Networks and Spatial Economics* | not applicable |
| 5 | **DSTF** | 2025 | DSTF: A Diversified Spatio-Temporal Feature Extraction Model for traffic flow prediction (https://doi.org/10.1016/j.neucom.2024.129280) | *Neurocomputing* | not reported |
| 6 | **KDE-HSMGCN** | 2025 | Heterogeneous-Scale Multi-Graph Convolutional Network Based on Kernel Density Estimation for Traffic Prediction (https://doi.org/10.1049/itr2.70042) | *IET Intelligent Transport Systems* | private (on request) |
| 7 | **LLGformer** | 2025 | LLGformer: Learnable Long-range Graph Transformer for Traffic Flow Prediction (https://doi.org/10.1145/3696410.3714596) | *Proceedings of the ACM on Web Conference 2025* | not reported |
| 8 | **MDEI-SSTGGAT** | 2025 | A synchronous spatiotemporal graph neural network for short-term traffic flow prediction (https://doi.org/10.1007/s00500-025-10555-6) | *Soft Computing* | not reported |
| 9 | **MSF-GODE** | 2025 | MSF-GODE: Multi-scale frequency-domain learning in graph neural ODEs for accurate traffic flow forecasting (https://doi.org/10.1016/j.neucom.2025.131566) | *Neurocomputing* | public: https://github.com/cloneyang886/MSF-GODE |
| 10 | **ReDyNet** | 2025 | Responsive Dynamic Graph Disentanglement for Metro Flow Forecasting (https://doi.org/10.1609/aaai.v39i11.33272) | *Proceedings of the AAAI Conference on Artificial Intelligence* | public (404/inactive): https://github.com/wangzz-yyzz/ReDyNet |
| 11 | **STFTGCN** | 2025 | Trend-aware spatio-temporal fusion graph convolutional network with self-attention for traffic prediction (https://doi.org/10.1016/j.neucom.2025.130040) | *Neurocomputing* | private (on request) |
| 12 | **STS-GraphSAGE** | 2025 | Spatial-temporal synchronous graphsage for traffic prediction (https://doi.org/10.1007/s10489-024-05970-5) | *Applied Intelligence* | private (on request) |
| 13 | **STSGNN** | 2025 | Designing Specialized Two-Dimensional Graph Spectral Filters for Spatial-Temporal Graph Modeling (https://doi.org/10.1609/aaai.v39i11.33251) | *Proceedings of the AAAI Conference on Artificial Intelligence* | public: https://github.com/Eighree/STSGNN |
| 14 | **STUM** | 2025 | Cross Space and Time: A Spatio-Temporal Unitized Model for Traffic Flow Forecasting (https://doi.org/10.1109/TITS.2025.3601630) | *IEEE Transactions on Intelligent Transportation Systems* | public: https://github.com/RWLinno/STUM |
| 15 | **StarG2N** | 2025 | StarG2N: a spatial-temporal relevance analysis graph neural network for traffic prediction (https://doi.org/10.1007/s10044-025-01519-5) | *Pattern Analysis and Applications* | public: https://github.com/Lance1999/StarG2N/tree/main |
| 16 | **CSHGCN** | 2026 | Causal-Enhanced Spatio-Temporal Markov Graph Convolutional Network for Traffic Flow Prediction (https://doi.org/10.3390/sym18020366) | *Symmetry* | not reported |
| 17 | **DG-STMTL** | 2026 | DG-STMTL: A novel graph convolutional network for multi-task spatio-temporal traffic forecasting (https://doi.org/10.1016/j.neucom.2025.132421) | *Neurocomputing* | not reported |
| 18 | **DMGGCN** | 2026 | A dynamic multi-dimensional globally aware graph convolutional network for traffic prediction (https://doi.org/10.1016/j.asoc.2026.115232) | *Applied Soft Computing* | public (404/inactive): https://github.com/Dx3281101/TrafficFlow-DMGGCN-main |
| 19 | **Fed-STSGCN** | 2026 | Federated Spatial-Temporal Synchronous Graph Convolutional Network for Cross-City Traffic Prediction (https://doi.org/10.1109/TCE.2026.3669705) | *IEEE Transactions on Consumer Electronics* | not reported |
| 20 | **GRU-GCN** | 2026 | Hybrid Graph Convolutional-Recurrent Framework with Community Detection for Spatiotemporal Demand Prediction in Micromobility Systems (https://doi.org/10.3390/math14010116) | *Mathematics* | not reported |
| 21 | **HSTGL** | 2026 | Integrating Heterogeneous Spatio-Temporal Interactions for Traffic Speed Prediction (https://doi.org/10.1145/3783987) | *ACM Transactions on Knowledge Discovery from Data* | not reported |
| 22 | **LAD-SGNN** | 2026 | LLM-Augmented Stiefel Graph Neural Networks for Zero-Shot Spatio-Temporal Forecasting (https://doi.org/10.1109/TKDE.2026.3689935) | *IEEE Transactions on Knowledge and Data Engineering* | public: https://github.com/komorebi424/DST-SGNN |
| 23 | **ST-Camba** | 2026 | ST-Camba: A decoupled-free spatiotemporal graph fusion state space model with linear complexity for efficient traffic forecasting (https://doi.org/10.1016/j.inffus.2025.103495) | *Information Fusion* | public: https://github.com/ai4city-sztu/ST-Camba |
| 24 | **STSA-GF** | 2026 | Short-term metro flow forecasting via spatiotemporal joint self-attention and multi-graph weighted fusion (https://doi.org/10.1016/j.ijtst.2025.11.001) | *International Journal of Transportation Science and Technology* | not reported |
| 25 | **STSAGNN** | 2026 | Spatio-temporal synchronous adaptive graph neural network for traffic demand forecasting (https://doi.org/10.1016/j.neucom.2026.133993) | *Neurocomputing* | public: https://github.com/kaiserliu6/STSAGNN |
| 26 | **TLSTS-GraphSAGE** | 2026 | Transfer Learning With Spatial-Temporal Synchronous Graph Sample and Aggregation for Traffic Prediction (https://doi.org/10.1109/JIOT.2025.3628859) | *IEEE Internet of Things Journal* | not reported |
| 27 | **TSGCN** | 2026 | Trajectory semantics-based graph convolutional network for taxi demand forecasting (https://doi.org/10.1016/j.ins.2025.123051) | *Information Sciences* | not reported |
| 28 | **Weaver** | 2026 | Weaver: Kronecker product approximations of spatiotemporal attention for traffic network forecasting (https://doi.org/10.1016/j.trc.2026.105825) | *Transportation Research Part C: Emerging Technologies* | private (on request) |

---
---

## 📖 Citation for Review Paper

```bibtex
@article{baker2026principled,
  title={Principled Unified Spatio-Temporal Graph Neural Networks for Traffic Forecasting: A Scoping Review},
  author={Baker, Clayton K. and Nyirenda, Clement N.},
  journal={Journal of Big Data},
  year={2026},
  publisher={Springer Nature},
  note={Under Review}
}
