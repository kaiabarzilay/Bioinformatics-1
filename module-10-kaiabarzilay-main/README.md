# BINF6308 Genome Assembly Module

Kaia Barzilay

## Methods

In this module, sequence data was retrieved using the NCBI Sequence Read Archive (SRA) and then assembled into a genome. In order to to this, the command-line utility fastq-dump [1] in the getNGS.sh script retrieved the genomic reads for Rhodobacter sphaeroides from SRA. 

Once the reads were retrieved, the next step was to trim them using Trimmomatic [2] in the trim.sh script with: paired-end reads, one server thread, removing 0 bases from the beginning, with a file of adapter sequences and the number of mismatches allowed in an adapter match (/usr/local/programs/Trimmomatic-0.36/adapters/TruSeq3-PE.fa:2:30:10), a minimum quality for trimming the start and end of reads of 20, a sliding window size of 4, a minimum average quality for the bases in that window of 30, and a minimum length for a read to be kept of 36. This script removed all of the adapter sequences and low-quality areas of the reads, placing the paired trimmed reads into a Paired directory. 

Once the reads were trimmed, the reads were assembled in the runSpades.sh script using SPAdes [3] a De Bruijn graph assembler, with a number of threads of 4 and an output directory of Rhodo. 

Once all of the trimmed reads were assembled, the script quest.sh used QUAST [4] to generate some summary statistics of the assembly with: the output of this script being a quast_output directory, splitting the scaffolds and adding contigs to the comparison, 4 threads, completing gene finding and a comparison to a reference genome /data/METHODS/Fall/Module10/GCF_000012905.2_ASM1290v2_genomic.fna.

## Conclusion from Analysis

The findings generated from using QUAST on the assembly had some interesting results. The N50 value for the scaffolds was 135342, and for the scaffolds_broken this was 127930. The N50 for the scaffolds was higher, which means that the genome has a better resolution and is the better sequence. This does make sense based on what we know about the scaffolds vs. the scaffolds_broken, as scaffolds_broken entailed the scaffolds being broken into contigs and then being assembled again [5]. In turn, the N50 value for the scaffolds being higher means that the shortest contig at 50% of the genome length was larger.

Various plots were graphed using the data from this assembly. The Nx plot for this assembly seemed to demonstrate that the scaffolds did have a slightly larger average contiguous length, however they are very similar. In addition, approximately 50% of the bases of the assembly were accounted for when contigs were larger than ~45 kbp. The GC content plot for this assembly represented the total number of G and C nucleotides divided by the length of the assembly. For this particular assembly, the largest number of windows were when the GC content was ~70%. The Cumulative length plot for this assembly demonstrated the number of bases in the contigs in relation to the number of contigs. This graph reflected a steady increase in the length of the contigs with the number of contigs. 

The total length of our scaffolds assembly was 4649099. When compared to the total size of the Rhodobacter sphaeroides of 4602977, it can be seen that the size of the scaffolds assembly was larger. The number of genes found by GeneMarkS was 4329, which was slightly smaller than the 4421 genes on the genome’s page on NCBI [6].

## Future Directions

Since QUAST generated a GFF file from this assembly, the next step would be to try and associate functions (GO terms) to the proteins. This could be done in some of the potential following ways (BINF6308, M9):

* Parsing the GFF file into FASTA format
* In order to get GO terms, use the downloadable files provided by UniProt to map the proteins to GO terms. 
* To get descriptions of the protein pathways and functions, first convert the SwissProt protein IDs, which are species-specific, into KEGG species-independent ortholog IDs.
* Get the KEGG Ortholog database ID from the protein IDs using the KEGG API.
* Use the KEGG Ortholog database ID to get the KEGG pathways associated with the KEGG orthology.
* Use the KEGG pathways to get descriptions of the KO pathways. 

## Citations

1. U.S. Department of Health and Human Services. (n.d.). Sra-Toolkit. National Institutes of Health. Retrieved April 19, 2022, from https://hpc.nih.gov/apps/sratoolkit.html 
2. Bolger, Lohse, M., & Usadel, B. (2014). Trimmomatic: a flexible trimmer for Illumina sequence data. Bioinformatics, 30(15), 2114–2120. https://doi.org/10.1093/bioinformatics/btu170
3. Bankevich, A., Nurk, S., Antipov, D., Gurevich, A. A., Dvorkin, M., Kulikov, A. S., Lesin, V. M., Nikolenko, S. I., Pham, S., Prjibelski, A. D., Pyshkin, A. V., Sirotkin, A. V., Vyahhi, N., Tesler, G., Alekseyev, M. A., & Pevzner, P. A. (2012, May). Spades: A new genome assembly algorithm and its applications to single-cell sequencing. Journal of computational biology : a journal of computational molecular cell biology. Retrieved April 19, 2022, from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3342519/ 
4. Gurevich, A., Saveliev, V., Vyahhi, N., & Tesler, G. (2013, April 15). Quast: Quality Assessment Tool for Genome Assemblies. Bioinformatics (Oxford, England). Retrieved April 19, 2022, from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3624806/ 
5. Quast 5.0.2 Manual. (n.d.). Retrieved April 19, 2022, from http://quast.sourceforge.net/docs/manual.html 
6. U.S. National Library of Medicine. (n.d.). Gene links for genome (select 509) - gene - NCBI. National Center for Biotechnology Information. Retrieved April 19, 2022, from https://www.ncbi.nlm.nih.gov/gene?LinkName=genome_gene&from_uid=509 
