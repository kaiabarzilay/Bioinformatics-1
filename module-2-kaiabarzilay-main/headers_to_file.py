#!/usr/bin/env python
# headers_to_file.py

# To use regular expressions you need to import re
import re

# Set the file path to the Drosophila genome
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'

# Initialize a line counter
line_count = 0

# Initialize a sequence variable
seq = ''

# Open the genome file
with open(dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        # If the line count is less than 50, print the line
        if line_count < 50:
            # Check to see if the line is a header line (starts with >)
            if re.match('^>', line):
                # Increase the line number to the next line
                line_count += 1
                # Append the line to 'seq' list
                seq += line

filename = "dmel_headers.txt"  # just the name of the file I'm going to write

# Open the file, and pass the 'w' parameter which means write to the file
with open(filename, 'w') as out:
    # Write the line of output
    out.write(seq)
   
