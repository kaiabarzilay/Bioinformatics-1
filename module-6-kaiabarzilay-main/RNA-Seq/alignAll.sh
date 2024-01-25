#!/usr/bin/env bash
# alignAll.sh

inputPath="/home/barzilay.k/BINF6308/module-6-kaiabarzilay/RNA-Seq/Paired"
outputPath="/home/barzilay.k/BINF6308/module-6-kaiabarzilay/RNA-Seq/sam"

# Initialize variables
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
sam="sam/"
alignAlllog="/alignAll.log"
alignAllerr="/alignAll.err"

# Create the output directories
mkdir -p $sam

# Align with GSNAP
function alignReads {
    for leftInFile in $inputPath*$leftSuffix
    do  
        # Remove the path from the filename and assign to pathRemoved
        pathRemoved="${leftInFile/$inputPath/}"
        # Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
        sampleName="${pathRemoved/$leftSuffix/}"
        # Print $sampleName to see what it contains after removing the path
        echo $sampleName       
        nice -n19 gsnap \
        -A sam \
        -D . \
        -d AiptasiaGmapDb \
        -s AiptasiaGmapIIT.iit \
        $inputPath$sampleName$leftSuffix \
        $inputPath$sampleName$rightSuffix \
        1>$outputPath$alignAlllog 2>$outputPath$alignAllerr
    done
}

alignReads 1>alignAll.log 2>alignAll.err
