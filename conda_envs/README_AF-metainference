# conda_AF-metainference 

Steps to create the conda environment and build the required software to replicate the WOX5 structural ensemble generation with the AF-metainference protocol (https://doi.org/10.1038/s41467-025-56572-9) 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Instructions on how to install/run your project. Example for a Python project:

```bash
git clone https://github.com/yourusername/project-name.git
cd project-name
pip install -r requirements.txt







conda create -n conda_AF-metainference python=3.11
conda activate conda_AF-metainference
conda install cuda-cudart cuda-version=12.2
conda install -y anaconda::gxx_linux-64
conda install -y -c conda-forge mpich mpi4py openmm=8.0 plumed=2.8.2=mpi_mpich_h7ded119_0 py-plumed cmake swig pandas mdtraj biopython matplotlib gromacs
conda install -y -c anaconda ipykernel
conda install -y -c bioconda pulchra

# Go to github_repos
git clone https://github.com/vendruscolo-lab/OpenMM-Plumed-MPI
cd OpenMM-Plumed-MPI/
mkdir build install openmm -p plumed/include -p plumed/lib
unzip openmm.zip -d openmm
unzip plumed_lib.zip -d plumed/lib
unzip plumed_include.zip -d plumed/include
cd build/
cmake ..
make
make install
export CPLUS_INCLUDE_PATH=$CONDA_PREFIX/lib/python3.11/site-packages/mpi4py/include:$CPLUS_INCLUDE_PATH
export C_INCLUDE_PATH=$CONDA_PREFIX/lib/python3.11/site-packages/mpi4py/include:$C_INCLUDE_PATH
make PythonInstall
cd ../install/lib
cp -r * /lustre/BIF/nobackup/perez070/miniconda3/envs/conda_AF-metainference/lib




