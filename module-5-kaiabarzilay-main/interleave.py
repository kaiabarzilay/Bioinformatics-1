#!/usr/bin/env python3
# interleave.py

# Import Seq, SeqRecord, and SeqIO
from Bio import SeqIO

# Import itertools to take a slice of list
import itertools

# Create arrays of left and right reads
leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
rightReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")

# Indicate to get all of the sequence
leftfile = itertools.islice(leftReads, None)
rightfile = itertools.islice(rightReads, None)

# Inititate a interleave variable
interleave = [ ]

# Iterate over both arrays in parallel
for left, right in zip(leftfile, rightfile):
        interleave.append(left)
        interleave.append(right)

# Write output to the Interleaved.fasta file
SeqIO.write(interleave, "Interleaved.fasta", "fasta")



