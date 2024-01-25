#!/usr/bin/env bash
# alignPredicted.sh

# Specify input path
blastp -query /home/barzilay.k/BINF6308/module-8-kaiabarzilay/BLAST/Trinity.fasta.transdecoder.pep \
    # Align to SwissProt
    -db /blastDB/swissprot \
    # limit to only the first five alignment 
    -num_alignments 5 \
    # Output in tabular format with specific fields
    -outfmt "6 qseqid sacc qlen slen length nident pident evalue < 1e-10 stitle"
    # Output to alignPredicted.txt file
    -out alignPredicted.txt
    1>alignPredicted.log 2>alignPredicted.err

