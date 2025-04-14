run_copilot <- function(samples, 
                        gene_list_path,
                        base_input_dir,
                        base_output_dir,
                        transcriptome = "TAIR10",
                        species = "Arabidopsis thaliana",
                        mt_pattern = "ATMG",
                        cp_pattern = "ATCG",
                        mt_threshold = 5,
                        filtering_ratio = 1) {

  # Load libraries
  library(Matrix)
  library(SeuratObject)
  library(Seurat)
  library(sctransform)
  library(COPILOT)

  # Load unwanted genes
  pp.genes <- as.character(read.table("/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/supp_data/Protoplasting_DEgene_FC2_list.txt", header = F)$V1)

  # Set memory options
  options(future.globals.maxSize = 4 * 1024^3)

  # Process each sample
  for (sample in samples) {
    sample.dir <- paste0(base_input_dir, "/", sample, "/final")
    output.dir <- paste0(base_output_dir, "/", sample)

    if (!dir.exists(output.dir)) {
      dir.create(output.dir, recursive = TRUE)
    }

    setwd(output.dir)
    print(getwd())

    copilot(
      sample.name = sample.dir,
      filtered.mtx.output.dir = output.dir,
      species.name = species,
      transcriptome.name = transcriptome,
      sample.stats = NULL,
      mt.pattern = mt_pattern,
      mt.threshold = mt_threshold,
      cp.pattern = cp_pattern,
      remove.doublet = TRUE,
      do.seurat = TRUE,
      do.annotation = FALSE,
      unwanted.genes = pp.genes,
      filtering.ratio = filtering_ratio
    )
  }
}


samples <- c('0h_1_scKB','0h_2_scKB','2h_1_scKB', '2h_2_scKB', '4h_1_scKB', '4h_2_scKB',
             '10h_1_scKB', '10h_2_scKB', '1d_1_scKB', '1d_2_scKB', '4d_1_scKB', '4d_2_scKB',
             '7d_1_scKB', '7d_2_scKB')

run_copilot(
  samples = samples,
  gene_list_path = "/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/supp_data/misc/Protoplasting_DEgene_FC2_list.txt",
  base_input_dir = "/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/output/1-2_scKB_mapping",
  base_output_dir = "/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/output/3-COPILOT"
)

