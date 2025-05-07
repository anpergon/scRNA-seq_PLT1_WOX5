# conda_scRNA-seq Environment Setup

This README provides instructions for creating and configuring the `conda_scRNA-seq` conda environment, designed for single-cell RNA sequencing (scRNA-seq) data analysis. This environment includes a comprehensive set of Python and R packages for various scRNA-seq analysis tasks.

## Prerequisites

* Conda installed on your system.
* CUDA-capable GPU (if using GPU acceleration for PyTorch and JAX).

## Installation Instructions

1.  **Create the Conda Environment:**

    ```bash
    conda create -n conda_scRNA-seq python=3.11 -y
    ```

    This command creates a new conda environment named `conda_scRNA-seq` with Python 3.11.

2.  **Activate the Conda Environment:**

    ```bash
    conda activate conda_scRNA-seq
    ```

    This command activates the `conda_scRNA-seq` environment.

3.  **Install Core Python Libraries:**

    ```bash
    conda install -c conda-forge numpy pandas matplotlib -y
    ```

    This installs essential Python libraries for data manipulation and visualization.

4.  **Install PyTorch with GPU Support:**

    ```bash
    conda install conda-forge::pytorch-gpu -y
    ```

    This installs PyTorch with GPU support.

5.  **Configure Channel Priority and Install JAX with CUDA:**

    ```bash
    conda config --set channel_priority flexible
    conda install "jaxlib=*=*cuda*" jax cuda-nvcc -c conda-forge -c nvidia -y
    conda install jax=0.4.26 -c conda-forge -y
    ```

    This configures channel priority and installs JAX with CUDA support for GPU acceleration.

6.  **Install scRNA-seq Analysis Libraries:**

    ```bash
    conda install -c conda-forge anndata scvi-tools scanpy python-igraph leidenalg scikit-image scikit-misc -y
    conda install bioconda::scvelo -y
    conda install -c conda-forge matplotlib=3.7.0 -y
    ```

    This installs key Python libraries for scRNA-seq data analysis, including Scanpy, scvi-tools, and scvelo.

7.  **Install Hyperopt and Ray Tune via pip:**

    ```bash
    $CONDA_PREFIX/envs/scRNA-seq_3/bin/pip install hyperopt
    $CONDA_PREFIX/envs/scRNA-seq_3/bin/pip install "ray[tune]"
    ```

    Install Hyperopt and Ray Tune using pip. *Adjust the path to your pip executable if needed.*

8.  **Install scib and scib-metrics:**

    ```bash
    conda install bioconda::scib -y
    $CONDA_PREFIX/envs/scRNA-seq_3/bin/pip install scib-metrics
    ```
    Install scib via conda, and scib-metrics via pip. *Adjust pip path if needed.*

9.  **Install PyTorch and Related Libraries (Specific CUDA Version):**

    ```bash
    conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y
    conda install pyg -c pyg -y
    conda install omicverse -c conda-forge -y
    conda remove matplotlib matplotlib-base
    conda install omicverse -c conda-forge -y
    conda install bioconda::scvelo -y
    ```

    Install PyTorch, PyG and omicverse. Remove and reinstall matplotlib to avoid possible conflicts.

10. **Install scvelo from GitHub:**

    ```bash
    $CONDA_PREFIX/envs/conda_scRNA-seq/bin/pip install git+ https://github.com/theislab/scvelo@main
    ```

    Install the main branch version of scvelo from GitHub. *Adjust the pip path to your pip executable if needed.

11. **Install rpy2 and r-seurat:**

    ```bash
    conda install -c conda-forge rpy2
    conda install conda-forge::r-seurat
    ```
    Installs rpy2, and the R seurat package.

## Notes

* Adjust the paths to your `pip` executable if necessary.
* Ensure that your GPU drivers are compatible with the specified CUDA versions.
