# conda_AF-metainference Setup

This README provides instructions for setting up the `conda_AF-metainference` conda environment, which includes dependencies for AlphaFold metainference and related tasks.

## Prerequisites

* Conda installed on your system.
* CUDA-capable GPU (if using GPU acceleration).
* Internet connection for downloading packages.
* Basic understanding of command-line operations.
* Access to the specified lustre directory `/lustre/BIF/nobackup/perez070/miniconda3/envs/`. Adjust the final copy path if your environment differs.

## Setup Instructions

1.  **Create and activate the conda environment:**

    ```bash
    conda create -n conda_AF-metainference python=3.11
    conda activate conda_AF-metainference
    ```

2.  **Install CUDA (if needed):**

    ```bash
    conda install cuda-cudart cuda-version=12.2
    ```

    * Adjust `cuda-version` to match your system's CUDA version if necessary.

3.  **Install essential system libraries:**

    ```bash
    conda install -y anaconda::gxx_linux-64
    ```

4.  **Install required packages:**

    ```bash
    conda install -y -c conda-forge mpich mpi4py openmm=8.0 plumed=2.8.2=mpi_mpich_h7ded119_0 py-plumed cmake swig pandas mdtraj biopython matplotlib gromacs
    conda install -y -c anaconda ipykernel
    conda install -y -c bioconda pulchra
    ```

5.  **Clone and build OpenMM-Plumed-MPI:**

    ```bash
    git clone [https://github.com/vendruscolo-lab/OpenMM-Plumed-MPI](https://github.com/vendruscolo-lab/OpenMM-Plumed-MPI)
    cd OpenMM-Plumed-MPI/
    mkdir build install openmm -p plumed/include -p plumed/lib
    unzip openmm.zip -d openmm
    unzip plumed_lib.zip -d plumed/lib
    unzip plumed_include.zip -d plumed/include
    cd build/
    cmake ..
    make
    make install
    ```

6.  **Set environment variables for MPI:**

    ```bash
    export CPLUS_INCLUDE_PATH=$CONDA_PREFIX/lib/python3.11/site-packages/mpi4py/include:$CPLUS_INCLUDE_PATH
    export C_INCLUDE_PATH=$CONDA_PREFIX/lib/python3.11/site-packages/mpi4py/include:$C_INCLUDE_PATH
    ```

7.  **Install Python bindings for OpenMM-Plumed-MPI:**

    ```bash
    make PythonInstall
    ```

8.  **Copy the built libraries to the conda environment:**

    ```bash
    cd ../install/lib
    cp -r * /lustre/BIF/nobackup/perez070/miniconda3/envs/conda_AF-metainference/lib
    ```

    * **Important:** Adjust the destination path (`/lustre/BIF/nobackup/perez070/miniconda3/envs/conda_AF-metainference/lib`) to match your conda environment's library directory.

## Notes

* Ensure that the zip files `openmm.zip`, `plumed_lib.zip`, and `plumed_include.zip` are present in the `OpenMM-Plumed-MPI/` directory before running the `unzip` commands.
* If you encounter any issues with package installations, check the Conda and package documentation for troubleshooting.
* Adjust CUDA version and paths according to your system.
* This setup is optimized for the specified environment. If you are working in a different setup, you may need to adjust the paths and package versions accordingly.
