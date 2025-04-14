import os
from pathlib import Path

def run_sckb_pipeline(samples, fastq_base_dir, src_dir, dest_dir):
    """
    Set up directories and run scKB mapping pipeline for a list of samples.

    Parameters:
    - samples: list of sample names
    - fastq_base_dir: path to base directory containing FASTQ folders (one per sample)
    - src_dir: path to directory containing source files (introns, tr2g, index, whitelist)
    - dest_dir: path to base output directory for results
    """
    # Define source files using src_dir
    src_file_introns = os.path.join(src_dir, "introns_tx_to_capture.txt")
    src_file_tr2g = os.path.join(src_dir, "tr2g.tsv")
    index_file = os.path.join(src_dir, "cDNA_introns_10xv3.idx")
    whitelist_file = os.path.join(src_dir, "10xv3_whitelist.txt")

    for sample in samples:
        print(f"Processing sample: {sample}")

        # Create sample output directory
        sample_output_dir = os.path.join(dest_dir, f"{sample}_scKB")
        os.makedirs(sample_output_dir, exist_ok=True)

        # Create symlinks for input files in the sample directory
        introns_symlink = os.path.join(sample_output_dir, "introns_tx_to_capture.txt")
        tr2g_symlink = os.path.join(sample_output_dir, "tr2g.tsv")

        if not os.path.exists(introns_symlink):
            os.symlink(src_file_introns, introns_symlink)
        if not os.path.exists(tr2g_symlink):
            os.symlink(src_file_tr2g, tr2g_symlink)

        # Define fastq directory for the current sample
        fastq_dir = os.path.join(fastq_base_dir, sample)

        # Output and log files
        final_output_dir = os.path.join(sample_output_dir, "final")
        log_file = os.path.join(sample_output_dir, f"output_{sample}_scKB.log")

        # Construct and execute the command
        cmd = (
            f"nohup {os.path.join(src_dir, 'scKB')} "
            f"-f {fastq_dir} "
            f"-i {index_file} "
            f"-d {sample_output_dir} "
            f"-s 10xv3 -t 8 "
            f"-w {whitelist_file} "
            f"-n {final_output_dir} "
            f"> {log_file} 2>&1 &"
        )

        os.system(cmd)



samples = ['0h_1', '0h_2', '2h_1', '2h_2', '4h_1', '4h_2', '10h_1', '10h_2', '1d_1', '1d_2', '4d_1', '4d_2', '7d_1', '7d_2']
fastq_base_dir = '/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/supp_data/PLT1-WOX5_samples'
src_dir = "/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/output/1-1_scKB_preparation"
dest_dir = "/lustre/BIF/nobackup/perez070/scRNA-seq_PLT1-WOX5/output/1-2_scKB_mapping"

run_sckb_pipeline(samples, fastq_base_dir, src_dir, dest_dir)




