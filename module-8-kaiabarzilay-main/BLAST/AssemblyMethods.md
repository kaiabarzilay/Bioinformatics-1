# Blast and Transdecoder

Kaia Barzilay

## Methods

For this module, the alignment tool BLAST was used to align the transcriptomes generated from the previous module to a BLAST database.

In order to do this weeks assignment, TransDecoder [1] was used to predict the proteins in the sequence before BLASTing. This was done by finding the longest reading frames and translating them into protein sequences, aligning these frames to SwissProt [2] a protein database and finally using hmmscan [3] and a Hidden Markov Model (HMM) to find protein domains. The output for this script was used for this weeks assignment.

The alignPredicted script created in this module aligns the output of Transdecoder. This output was aligned against against SwissProt [2], with a filter being set for evalue < 1e-10 and an output in a tabular format with the fields qseqid, sacc, qlen, slen, length, nident, pident, evalue and stitle. This script was not run to blasp using max_target_seqs 1. Output for this script is directed to alignPredicted.txt.

### Citations

1. Menor, C. (2020, February 4). Predict coding regions in OmicsBox with TransDecoder. BioBam. Retrieved April 4, 2022, from https://www.biobam.com/predicting-coding-regions-within-transcripts-in-omicsbox-with-transdecoder/?cn-reloaded=1 

2.  McMillan, & Martin, A. C. R. (2008). Automatically extracting functionally equivalent proteins from SwissProt. BMC Bioinformatics, 9(1), 418–418. https://doi.org/10.1186/1471-2105-9-418

3. Home. ManKier. (n.d.). Retrieved April 4, 2022, from https://www.mankier.com/1/hmmscan  









