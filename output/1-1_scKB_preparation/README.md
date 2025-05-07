# scKB Installation and Preparation Guide

This README provides step-by-step instructions for obtaining the necessary files to run the scKB analysis pipeline, primarily based on the [Hsu-Che-Wei/scKB](https://github.com/Hsu-Che-Wei/scKB) repository.

## Prerequisites

* Conda installed on your system.
* R installed within the conda environment.

## Installation and Preparation Steps

1.  **Clone the scKB Repository:**

    Open your terminal and navigate to the directory where you keep your GitHub repositories. Then, clone the scKB repository:

    ```bash
    cd /path/to/your/directory/github_repositories
    git clone https://github.com/Hsu-Che-Wei/scKB.git
    cd ./scKB
    ```

2.  **Download and Extract Whitelist Files:**

    Navigate to the directory where you intend to prepare the scKB input files (we'll refer to this as `/path/to/your/directory/1-1_scKB_preparation`). Download and extract the 10x V2 and V3 whitelist files:

    ```bash
    unzip /path/to/your/directory/github_repositories/scKB/10xv2_whitelist.txt.zip -d /path/to/your/directory/1-1_scKB_preparation
    unzip /path/to/your/directory/github_repositories/scKB/10xv3_whitelist.txt.zip -d /path/to/your/directory/1-1_scKB_preparation
    ```

3.  **Download and Extract Arabidopsis GTF File:**

    Download and extract the Arabidopsis thaliana TAIR10 GTF file:

    ```bash
    gunzip -c /path/to/your/directory/github_repositories/scKB/Arabidopsis_thaliana.TAIR10.43.gtf.gz > /path/to/your/directory/1-1_scKB_preparation/Arabidopsis_thaliana.TAIR10.43.gtf
    ```

4.  **Make scKB Executable and Copy:**

    Navigate back to the cloned `scKB` repository and make the `scKB` script executable. Then, copy it to your preparation directory:

    ```bash
    cd /path/to/your/directory/github_repositories/scKB
    chmod 777 scKB
    cp scKB /path/to/your/directory/1-1_scKB_preparation
    ```

5.  **Create and Install Conda Environment:**

    The scKB pipeline has specific dependencies. It is highly recommended to create a dedicated conda environment. Refer to the `README_scKB` file located in the `conda_envs` directory for instructions on how to create and install the necessary packages in a conda environment.


6.  **Run R for Velocity File Generation and Kallisto Indexing:**

    Activate the conda environment you created in the previous step. Then, open R within that environment. Navigate to your scKB preparation directory and execute the following R code:

    ```R
    # Activate your conda environment (if not already active)
    # conda activate your_scKB_env_name

    # Start R
    R

    # Inside R:
    setwd('/path/to/your/directory/1-1_scKB_preparation')
    library(BUSpaRse)
    library(BSgenome.Athaliana.TAIR.TAIR9)

    # Generate velocity files
    get_velocity_files(X = "./Arabidopsis_thaliana.TAIR10.43.gtf", L = 91, Genome = BSgenome.Athaliana.TAIR.TAIR9, out_path = "./", isoform_action = "separate", chrs_only=FALSE, style="Ensembl")

    # Index cDNA and introns for kallisto
    system("kallisto index -i ./cDNA_introns_10xv3.idx ./cDNA_introns.fa")

    # Exit R
    q()
    ```

## Next Steps

After completing these steps, you should have the necessary whitelist files, the Arabidopsis GTF file, the executable `scKB` script, a configured conda environment, generated velocity files, and a kallisto index. You can then proceed with running the scKB pipeline according to the documentation and scripts within the [Hsu-Che-Wei/scKB](https://github.com/Hsu-Che-Wei/scKB) repository.

## Notes

* Pay close attention to the instructions in the `README_scKB` file for setting up the conda environment, as specific package versions might be required.
* This guide assumes you are working with Arabidopsis data. The `get_velocity_files` function and genome package might need to be adjusted for other organisms.
