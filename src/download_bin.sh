#!/bin/bash

url="https://github.com/tabulapdf/tabula-java/releases/download/v1.0.3/tabula-1.0.3-jar-with-dependencies.jar"
outdir="./bin"

wget -P ${outdir} ${url}

