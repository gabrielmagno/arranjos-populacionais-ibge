#!/bin/bash

url="https://www.ibge.gov.br/apps/arranjos_populacionais/2015/pdf/publicacao.pdf"
outdir="./raw"

wget -P ${outdir} ${url}

