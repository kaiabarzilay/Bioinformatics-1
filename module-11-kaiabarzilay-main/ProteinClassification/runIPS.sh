#!/usr/bin/env bash
# runIPS.sh

# Change the path for the script
PATH="/usr/local/programs/jdk-11.0.9/bin/:$PATH"
export PATH

# Write a function
function scan {
     # Use proteins.fasta as input
     # Add GO terms
     # Disable the InterProScan Lookup Match Service
     # CPUs 4
     # Produce proteins.tsv as output in the .tsv format
     interproscan.sh \
     --input proteins.fasta \
     --goterms \
     --disable-precalc \
     --cpu 4 \
     --outfile proteins.tsv \
     --formats TSV 
}
scan 1>scan.log 2>scan.err
