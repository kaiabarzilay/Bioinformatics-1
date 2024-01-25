#!/usr/bin/env python3
# find_dmel_orf.py
# Import seq
from Bio import SeqIO
# Import seq
from Bio.Seq import Seq

# Import re
import re

# Identify sequence
infile = "/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta"

for record in SeqIO.parse(infile, "fasta"):
    # Check to see that there are no scaffold sequences
    if re.match("^\d{1}\D*$", record.id):

        # Transcribe from DNA to RNA
        dna = record.seq
        rna = dna.transcribe()

        # Find the Open Reading Frame (ORF)
        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()

        # Create seq from string pbject orf
        orf_seq = Seq(orf)

        # Transate the Open Reading Frame (ORF) to a protein
        protein = orf_seq.translate()

        # Print protein
        print(protein)

