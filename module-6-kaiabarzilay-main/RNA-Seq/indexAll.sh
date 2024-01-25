#1/usr/bin/env bash
# indexAll.sh

inputPath="/home/barzilay.k/BINF6308/module-6-kaiabarzilay/RNA-Seq/bam"

#Initialize variable 
indexAlllog="/indexAll.log"
indexAllerr="/indexAll.err"

function indexAll {
    for file in $inputPath
    do
        samtools index file
        1> $inputPath$indexAlllog 2> $inputPath$indexAllerr
    done

}
indexAll 1>indexAll.log 2>indexAll.err
