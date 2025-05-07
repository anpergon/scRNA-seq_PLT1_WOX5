# conda_COPILOT Environment Setup

This README provides instructions for setting up the `conda_COPILOT` conda environment, which includes dependencies for COPILOT and related single-cell RNA sequencing (scRNA-seq) analysis tasks.

## Prerequisites

* Conda installed on your system.
* R installed within the conda environment.

## Setup Instructions

1.  **Create and activate the conda environment:**

    ```bash
    conda create -n conda_COPILOT -c conda-forge r-base=4.3.2 r-essentials -y
    conda activate conda_COPILOT
    ```

2.  **Install core R and Python dependencies:**

    ```bash
    conda install -c conda-forge umap-learn \
        r-seurat \
        r-devtools \
        r-rjson \
        r-r2html \
        bioconductor-dropletutils
    ```

3.  **Install additional R packages from Bioconda and conda-forge:**

    ```bash
    conda install bioconda::r-leidenbase
    conda install -c conda-forge r-igraph
    ```

4.  **Install COPILOT and DoubletFinder from GitHub using `devtools`:**

    ```R
    devtools::install_github('chris-mcginnis-ucsf/DoubletFinder')
    devtools::install_github('ohlerlab/COPILOT')
    ```

5.  **Install `glmGamPoi` from Bioconductor:**

    ```R
    install.packages('BiocManager')
    BiocManager::install('glmGamPoi')
    ```

6.  **Install the Python `umap-learn` package within the R environment:**

    ```R
    library(reticulate)
    py_install("umap-learn")
    ```

7.  **Modify the COPILOT directory to avoid problems related to incompatibilities of DoubletFinder versions:**


8.  **Install the local COPILOT package from the specified directory to avoid the problem with DoubletFinder:**

    ```R
    devtools::install("/path/to/your/directory/scRNA-seq_PLT1-WOX5/github_repositories/COPILOT")
    ```
