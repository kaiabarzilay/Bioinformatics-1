#!/usr/bin/env bash
# runQuast.sh

/usr/bin/quast.py \
    -o quast_output \
    -s Rhodo/scaffolds.fasta \
    -t 4 \
    -f \
    -R /data/METHODS/Fall/Module10/GCF_000012905.2_ASM1290v2_genomic.fna \

