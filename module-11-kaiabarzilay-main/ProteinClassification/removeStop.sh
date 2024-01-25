#!/usr/bin/env bash
# removeStop.sh

# Read in Trinity.fasta.transdecoder.pep from the BLAST directory
# Remove the * characters using sed
# Output the first 5000 lines to proteins.fasta
sed 's/*//' Trinity.fasta.transdecoder.pep | head -n 5000 > proteins.fasta 

