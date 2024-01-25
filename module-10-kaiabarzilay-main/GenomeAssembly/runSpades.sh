#!/usr/bin/env bash
# runSpades.py

/usr/local/programs/SPAdes-3.14.1-Linux/bin/spades.py \
    -o Rhodo \
    -1 SRR522244_1.fastq \
    -2 SRR522244_2.fastq \
    --only-assembler \
    --careful \
    --threads 4 \
    1>runSpades.log 2>runSpades.err
