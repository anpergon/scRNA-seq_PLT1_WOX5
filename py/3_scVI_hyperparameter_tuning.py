# Import libraries and dependencies
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import scanpy as sc
import torch
import scvi
import scvelo as scv
import anndata
import re
import seaborn as sns
import ray
from ray import tune
from scvi import autotune

os.environ["CUDA_VISIBLE_DEVICES"] = "1"



# Matrix multiplication balancing precision and computational efficiency (options: medium-high-highest)
torch.set_float32_matmul_precision("high")

# Highest level of verbosity
sc.settings.verbosity = 3  

# Reproducibility
scvi.settings.seed = 1

# Figures
scv.set_figure_params(style="scvelo")

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')



# Select samples
os.chdir('/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/output/1-2_scKB_mapping')
samples = ['0h_1_scKB','0h_2_scKB','2h_1_scKB','2h_2_scKB','4h_1_scKB','4h_2_scKB','10h_1_scKB','10h_2_scKB']

# Retrieve sample name for Shahan et al. (2022) atlas
shahan_directory = "/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/supp_data/Shahan_samples"
shahan_ids = sorted([f.replace(".rds", "") for f in os.listdir(shahan_directory) if f.endswith(".rds")])
shahan_samples = [re.search(r'GSE152766_(.*?)_COPILOT', item).group(1) for item in shahan_ids]

# Needed to annotate the Shahan et al. (2022) atlas
analysis_dir = '/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/supp_data/misc/'
sample_labels = pd.read_csv(f'{analysis_dir}/samples.txt',sep='\t',header=None,index_col=0,names=['label','idx'])


# Read preprocessed Anndata object
adata = anndata.read_h5ad('/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/output/3-2_anndata_obj/scVI_scANVI_1.h5ad')



# Initialize scVI
model_tuning = scvi.model.SCVI
model_tuning.setup_anndata(adata, batch_key='sample')


# Set of hyperparameters to be tested
search_space = {
    "model_params": {"n_hidden": tune.choice([64, 128, 256]), "n_latent": tune.choice([10, 20, 30]), 
                     "n_layers": tune.choice([1, 2, 3, 4]), "dispersion": tune.choice(["gene", "gene-batch", "gene-label", "gene-cell"]),
                     "gene_likelihood": tune.choice(["nb", "zinb"])
                     },
    "train_params": {"max_epochs": 100, "train_size": 0.9, "validation_size": 0.1, "early_stopping": True, "early_stopping_patience": 10,
                     "batch_size": tune.choice([64, 128, 256]), "plan_kwargs": {"lr": tune.choice([0.005, 0.001, 0.0005])}}
}

# Hyperparameter tuning
tuning = scvi.autotune.run_autotune(
    model_tuning, 
    adata, 
    metrics = "elbo_validation", 
    mode = "min", 
    search_space = search_space,
    num_samples=150,
    searcher = "hyperopt",
    resources = {"cpu":60.0, "gpu":1.0}
    )


# Print the results
print(tuning.result_grid)



