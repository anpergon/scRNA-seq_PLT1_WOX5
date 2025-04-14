# conda_COPILOT Setup

This README provides instructions for setting up the `conda_COPILOT` conda environment, which includes dependencies for COPILOT and related single-cell RNA sequencing (scRNA-seq) analysis tasks.

## Prerequisites

* Conda installed on your system.
* R installed within the conda environment.
* Internet connection for downloading packages.
* Basic understanding of command-line operations and R package installation.
* Access to the specified lustre directory `/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/github_repositories/COPILOT`. Adjust the final installation path if your environment differs.

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

7.  **Install the local COPILOT package from the specified directory:**

    ```R
    devtools::install("/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/github_repositories/COPILOT")
    ```

    * **Important:** Adjust the installation path (`/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/github_repositories/COPILOT`) to match the location of your local COPILOT package.

## Notes

* Ensure that you have access to the specified lustre directory for the final installation step.
* If you encounter any issues with package installations, check the Conda, Bioconductor, and R package documentation for troubleshooting.
* This setup is optimized for the specified environment. If you are working in a different setup, you may need to adjust the paths and package versions accordingly.
* The `reticulate` step ensures that the Python `umap-learn` package is available for use within R.
* The final installation step assumes that the COPILOT package is present as a source package in the specified directory.
* If you are installing COPILOT from a different location, please change the path accordingly.
