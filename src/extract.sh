#!/bin/bash

bindir="./bin"
binfile="${bindir}/tabula-1.0.3-jar-with-dependencies.jar"

indir="./raw"
infile="${indir}/publicacao.pdf"

outdir="./data"
outfile="${outdir}/aglomerados-raw.csv"

java -jar "${binfile}" --area %13,0,100,29 --pages 72-96 "${infile}" > "${outfile}"
java -jar "${binfile}" --area %13,0,56,29 --pages 97 "${infile}" >> "${outfile}"

