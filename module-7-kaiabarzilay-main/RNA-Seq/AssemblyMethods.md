# Transcriptome Assembly

Kaia Barzilay

## Methods

Within this module, the quality-trimmed reads in the bam format were used to assemble a reference-guided transcriptome and a de-novo transcriptome. In order to make a reference-guided transcriptome, the reads were first merged into a single bam file using samtools [1] in order to ensure that only samples with Aip in the name were included. The merged bam file was then assembled using Trinity [2] with 1000 being the maximum separation distance Trinity allowed for segments of the transcript to span introns, a maximum assembly memory of 10G and CPU of 4. The N50 for this assembly was 574. In order to make a de-novo transcriptome, the reads needed to be seperated into two lists for left and right reads that were comma-seperated. Once the two lists were created,the reads were assembled using Trinity de-novo [2] with 4 CPUs. The N50 for this assembly was 510, which was smaller than the N50 value derived from the reference-guided transcriptome.   

## References 

1.   Li, Handsaker, B., Wysoker, A., Fennell, T., Ruan, J., Homer, N., Marth, G., Abecasis, G., & Durbin, R. (2009). The Sequence Alignment/Map format and SAMtools. Bioinformatics, 25(16), 2078–2079. https://doi.org/10.1093/bioinformatics/btp352

2.   Grabherr, Haas, B. J. B. J., Yassour, M. M., Levin, J. Z. J. Z., Thompson, D. A. D. A., Amit, I. I., Adiconis, X. X., Fan, L. L., Raychowdhury, R. R., Zeng, Q. Q., Chen, Z. Z., Mauceli, E. E., Hacohen, N. N., Gnirke, A. A., Rhind, N. N., di Palma, F. F., Birren, B. W. B. W., Nusbaum, C. C., Lindblad-Toh, K. K., … Regev, A. A. (2011). Trinity: reconstructing a full-length transcriptome without a genome from RNA-Seq data. Nature Biotechnology, 29(7), 644–652. https://doi.org/10.1038/nbt.1883



