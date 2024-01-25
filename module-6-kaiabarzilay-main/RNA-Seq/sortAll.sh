#!/usr/bin/env bash
# sortAll.sh

inputPath="/home/barzilay.k/BINF6308/module-6-kaiabarzilay/RNA-Seq/sam"
outputPath="/home/barzilay.k/BINF6308/module-6-kaiabarzilay/RNA-Seq/bam"

# Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
bam="bam/"
samPath="sam/"
sam=".sam"
sorted_bam=".sorted.bam"
sortAllLog="/sortAll.log"
sortAllErr="/sortAll.err"

# Create the output directory
mkdir -p $bam

function sortAll {
    for file in $inputPath
    do
        fileBase=${$file/$sam/}
        samtools sort \
        $file \
        -o $fastqPath$bam$fileBase$sorted_bam \
        1>$outputPath$sortAllLog 2>$outputPath$sortAllErr
    done
}
sortAll 1>sortAll.log 2>sortAll.err
