# conda_sceasy Environment Setup

This repository provides instructions for creating a conda environment named `conda_sceasy` to support the use of the R package `sceasy` and its dependencies.

## Overview

The `sceasy` R package facilitates the conversion of single-cell data between various formats, including AnnData (`.h5ad`), SingleCellExperiment (`.rds`), and Seurat objects (`.rds`). This conda environment streamlines the installation of `sceasy` and its necessary dependencies, ensuring a consistent and reproducible analysis environment.

## Installation Instructions

Follow these steps to create and configure the `conda_sceasy` environment:

1.  **Create the Conda Environment:**

    ```bash
    conda create --name conda_sceasy r-base
    ```

    This command creates a new conda environment named `conda_sceasy` with the base R installation.

2.  **Activate the Conda Environment:**

    ```bash
    conda activate conda_sceasy
    ```

    This command activates the newly created `conda_sceasy` environment.

3.  **Install AnnData (Python):**

    ```bash
    conda install anndata -c bioconda
    ```

    AnnData is a Python library used for handling annotated data matrices, which is a dependency for `sceasy` when working with `.h5ad` files.

4.  **Install sceasy (R):**

    ```bash
    conda install -c bioconda r-sceasy
    ```

    This command installs the `sceasy` R package from the bioconda channel.

5.  **Install R Essentials:**

    ```bash
    conda install -c conda-forge r-essentials
    ```

    This installs a collection of commonly used R packages, which are often required for general R usage and may be needed by `sceasy` and its dependencies.

## Usage

After successfully creating and activating the `conda_sceasy` environment, you can use R and Python within this environment. To use `sceasy`, open R within the activated environment and load the library:

```R
library(sceasy)

