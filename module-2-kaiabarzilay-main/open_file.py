#!/usr/bin/env python
# open_file.py

# Set the file path to the Drosophila genome
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'

# if I was developing locally I could paths and pound one out ('you've scp'd the fasta file locally)
# to get the file I would scp barzilay.k@defiance.neu.edu:/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta .
#dmel_genome_path = '/your_dir/locally/dmel-all-chromosome-r6.17.fasta'

# Inititalize a line counter
line_count = 0

# Open the genome file
with open(dmel_genome_path) as dmel_genome:
    # Iterate over the lines in the file
    for line in dmel_genome:
        # Increment the line count by one
        line_count += 1
        # If the line count is less than 5, print the line 
        if line_count < 5:
            print(line)
