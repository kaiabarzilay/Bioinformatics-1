# Short Read Alignment

Kaia Barzilay

## Methods

Reads were quality trimmed using Trimmomatic [1] with paired-end reads, one server thread, the left read files /scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq, the right read files /scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq, the output files for paired output (Aip02.R1.paired.fastq and Aip02.R2.paired.fastq and the output files for the unpaired output (Aip02.R2.unpaired.fastq and Aip02.R1.unpaired.fastq), removing 0 bases from the beginning, with a file of adapter sequences and the number of mismatches allowed in an adapter match (/usr/local/programs/Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10), a minimum quality for trimming the start and end of reads of 20, a sliding window size of 4, a minimum average quality for the bases in that window of 30, and a minimum length for a read to be kept of 36. Reads were aligned with gsnap [2] and alignments were sorted and indexed with samtools [3]. 

## References

1. 
  Bolger, Lohse, M., & Usadel, B. (2014). Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics (Oxford, England), 30(15), 2114–2120. https://doi.org/10.1093/bioinformatics/btu170

2.
  Wu, & Nacu, S. (2010). Fast and SNP-tolerant detection of complex variants and splicing in short reads. Bioinformatics, 26(7), 873–881. https://doi.org/10.1093/bioinformatics/btq057
 
3. 
  Li, Handsaker, B., Wysoker, A., Fennell, T., Ruan, J., Homer, N., Marth, G., Abecasis, G., & Durbin, R. (2009). The Sequence Alignment/Map format and SAMtools. Bioinformatics, 25(16), 2078–2079. https://doi.org/10.1093/bioinformatics/btp352
