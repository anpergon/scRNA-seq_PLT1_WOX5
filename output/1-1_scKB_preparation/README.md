cd /path/to/your/github_repositories_directory

git clone https://github.com/Hsu-Che-Wei/scKB.git

cd ./scKB

unzip 10xv2_whitelist.txt.zip -d /path/to/your/scKB_preparation_directory
unzip 10xv3_whitelist.txt.zip -d /path/to/your/scKB_preparation_directory

gunzip -c Arabidopsis_thaliana.TAIR10.43.gtf.gz > /path/to/your/scKB_preparation_directory/Arabidopsis_thaliana.TAIR10.43.gtf

chmod 777 scKB

cp scKB /path/to/your/scKB_preparation_directory



# Create a conda environment and install the required packages (see README_scKB in directory conda_envs)


R
# In R

setwd('/path/to/your/scKB_preparation_directory')

library(BUSpaRse)
library(BSgenome.Athaliana.TAIR.TAIR9)

get_velocity_files(X = "./Arabidopsis_thaliana.TAIR10.43.gtf", L = 91, Genome = BSgenome.Athaliana.TAIR.TAIR9, out_path = "./", isoform_action = "separate", chrs_only=FALSE, style="Ensembl")

system("kallisto index -i ./cDNA_introns_10xv3.idx ./cDNA_introns.fa")



