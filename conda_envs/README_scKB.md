# conda_scKB Environment Setup (for scKB Repository)

This repository provides instructions for creating a conda environment named `conda_scKB` designed to run mapping with scKB, a wrapper script of Kallisto and Bustools: [scKB](https://github.com/ohlerlab/scKB) repository.

## Overview

This conda environment can be used to run scKB mapping

## Installation Instructions

1.  **Clone the scKB Repository:**

    ```bash
    git clone [https://github.com/ohlerlab/scKB.git](https://github.com/ohlerlab/scKB.git)
    cd scKB
    ```

2.  **Create the Conda Environment:**

    Ensure you are in the `scKB` repository directory. Then, execute:

    ```bash
    conda env create -f scKB.yml
    ```

    This command creates the `conda_scKB` environment using the specifications from `scKB.yml`. If you don't modify the file your conda environment will be "scKB"

3.  **Activate the Conda Environment:**

    ```bash
    conda activate conda_scKB
    ```

    This command activates the `conda_scKB` environment.

4.  **Clean Conda Cache (Optional but Recommended):**

    ```bash
    conda clean --all
    ```

    This command cleans the conda cache, which can free up disk space and resolve potential dependency issues.

5.  **Remove Base R and Install devtools:**

    ```bash
    conda remove r-base
    conda install -c conda-forge r-devtools
    ```

    This removes the base R installation that may have been automatically installed and installs devtools from conda-forge.

6.  **Install BUSpaRse and Genome Packages (R):**

    Open R within the activated `conda_scKB` environment. Then, execute the following R code:

    ```R
    if (!requireNamespace("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
    if (!require(devtools)) install.packages("devtools")

    devtools::install_github("BUStools/BUSpaRse")
    BiocManager::install("BSgenome")

    # Install Arabidopsis TAIR genome
    BiocManager::install("BSgenome.Athaliana.TAIR.TAIR9")

    # Install Rice MSU genome
    BiocManager::install("BSgenome.Osativa.MSU.MSU7")

    # Load the genomes as BSgenome object
    library(BSgenome.Athaliana.TAIR.TAIR9)
    library(BSgenome.Osativa.MSU.MSU7)

    # Check the genomes (Optional)
    BSgenome.Athaliana.TAIR.TAIR9
    BSgenome.Osativa.MSU.MSU7
    ```

    This R code installs the necessary packages, including BUSpaRse, BSgenome, and the genome-specific packages for Arabidopsis and Rice.

## Usage

After installation, you can proceed with the preparation of the input files for scKB
