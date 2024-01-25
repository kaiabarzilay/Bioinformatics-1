#!/usr/bin/env python
# count_aip_kmers.py

# Import re
import re

# Open the file
filename = '/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq'

with open(filename, 'r') as count_aip_kmers:
    for line in count_aip_kmers:
        # get rid of the hidden new line character
        line = line.rstrip()

        if re.match('^[ATGCN]+$', line):
            # assign line as seq
            seq = line

kmer_length = 6

# Initialize a kmer dictionary
kmer_dictionary = {}

# Calculate the stop before the loop to improve efficiency
stop = len(seq) - kmer_length + 1

# Iterate over the positions
for start in range(0, stop):
    # Get the substring at a specific start and end position
    kmer = seq[start:start + kmer_length]
    
    # See if it's in the dictionary
    if kmer in kmer_dictionary:
        # Add one to the count
        kmer_dictionary[kmer] += 1
    else:
        # It's not in the dictionary so add with a count of 1
        kmer_dictionary[kmer] = 1

# Save a tab character to print output as tab-seperated
t = "\t"

# Iterate over the kmers in the dictionary
for kmer in kmer_dictionary:
    # Get the count of how many times observed
    count = kmer_dictionary[kmer]
    # Convert the count to a string and make a tuple of the kmer and count
    out = (kmer, str(count))
    # Join the elements of the out tuple with tabs and create output
    line_to_write = (t.join(out))
   
# The name of the file I am going to write
filename = "aip_kmers.txt" 

# Open the file, and pass the 'w' parameter which means write to the file
with open(filename, 'w') as out:
    # Write the line of output
    out.write(line_to_write)
