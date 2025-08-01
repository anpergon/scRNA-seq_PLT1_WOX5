# scRNA-seq_PLT1_WOX5

## Overview

This repository contains the analysis pipeline and supporting files for our single-cell RNA sequencing (scRNA-seq) study exploring early transcriptional reprogramming in *Arabidopsis thaliana* root cells following the overexpression of two key transcription factors: PLT1 and WOX5. The study aims to dissect the cellular dynamics and gene regulatory mechanisms involved in cell fate transitions during early root regeneration.

## Objectives

- Explain the cellular trajectories from root tissue to callus after *PLT1*-*WOX5* overexpression during a 10-hour window (and the underlying transcriptional programs).
- Study the interaction between PLT1 and WOX5 to explain the main features involved in it and discuss the possible biological implications.

## Key Findings

- **Cell Identity Changes**: *PLT1*-*WOX5* overexpression triggers rapid and specific changes in root cell identities indicated by the KL divergence-weighted cosine distance calculation.
- **Gene Regulatory Networks**: a subset of cells that putatively originate from XPP cells shows activation of Cajal body-related genes and ribosome biogenesis, indicating a trend towards dedifferentiation.
- **Structural Modeling**: AlphaFold-metainference accurately generates a structural ensemble for WOX5.

## Repository Content
* **`R/`:** contains the code to run COPILOT
* **`conda_envs`:** contains instructions to install all the conda environments used in this study
* **`jupyter_notebooks/`:** contains .ipynb files, including:
    * AF_metainference: generation of WOX5 structural ensemble.
    * CellRank: cell fate probabilities estimation.
    * rds_to_RData and RData_to_h5ad: two consecutive notebooks to convert Seurat objects to Anndata objects
    * correlation_analysis: KL divergence-weighted cosine distances.
    * scTour: pseudotime analysis. 
    * scVI_scANVI: cell type and developmental stage annotation.
    * scVelo: RNA velocity analysis.
* **`output/`:** contains the output of our analysis:
    * 1-1_scKB_preparation: instructions to prepare the files for scKB mapping.
    * 4-MINI-EX: PLT1-WOX5 shared targets at 10 hours in cluster Unknown4.
* **`py/`:** Contains code in Python:
    * 1_scKB: code to run scKB mapping.
    * 3_scVI_hyperparameter_tuning: code to run hyperparameter tuning
* **`supp_data/misc`:** Contains supplementary data used in the project such as the set of genes identified as protoplasting-associated
* **`README.md`:** This file, providing an overview of the repository.


## Pipeline
* **`1-scKB/`:** create conda_scKB environment, prepare the input files according to output/1-1_scKB_preparation and run scKB mapping with py/1_scKB.py
* **`2-COPILOT/`:** create conda_COPILOT environment and use the output from 1-scKB to run COPILOT with the function in R/2-COPILOT.R
* **`3-scVI/`:** create conda_scRNA_seq environment and run the correlation analysis with jupyter_notebooks/3-1_correlation_analysis.ipynb, then run cell type and developmental stage prediction with jupyter_notebooks/3-2-scVI_scANVI.ipnyb and hyperparameter tuning with py/3_scVI_hyperparameter_tuning.py. Next, run RNA velocity analyses with jupyter_notebooks/3-3_scVelo.ipynb, pseudotime inference with jupyter_notebooks/3-4_scTour.ipynb and cell fate probability estimation with jupyter_notebooks/3-5_CellRank.ipynb
* **`4-MINI-EX/`:** prepare dataset for MINI-EX run with jupyter_notebooks/4-1_MINI-EX_preparation.ipynb and run according to MINI-EX repository
* **`5-AF_metainference/`:** create the conda_AF_metainference environment run Alphafold-metainference protocol with jupyter_notebooks/5_AF_metainference.ipnyb


