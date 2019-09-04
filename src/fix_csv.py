#!/usr/bin/env python3

import csv
import json

OUTDIR = "./data"

INFILE_NAME = "{}/aglomerados-raw.csv".format(OUTDIR)
OUTFILE_JSON = "{}/aglomerados.json".format(OUTDIR)
OUTFILE_CSV = "{}/aglomerados.csv".format(OUTDIR)

aglomerados = {}

with open(INFILE_NAME, "r") as infile:
    csvr = csv.reader(infile)

    actual_rowtype = None
    last_rowtype = None

    aglomerado_nome = None 

    for nome, codigo in csvr:

        actual_rowtype = "c" if codigo else "a"

        if actual_rowtype == "a":

            if last_rowtype == "c" or not last_rowtype:

                if last_rowtype == "c":
                    aglomerados[aglomerado_nome] = aglomerado_cidades

                aglomerado_nome = nome
                aglomerado_cidades = []

            if last_rowtype == "a":

                aglomerado_nome = "{} {}".format(aglomerado_nome, nome)

        elif actual_rowtype == "c":
            nome_simple = nome[:-5]
            estado = nome[-3:-1]
            aglomerado_cidades.append([codigo, estado, nome_simple])

        last_rowtype = actual_rowtype

aglomerados[aglomerado_nome] = aglomerado_cidades

with open(OUTFILE_JSON, "w") as outfile:
    json.dump(aglomerados, outfile)

with open(OUTFILE_CSV, "w") as outfile:
    csvw = csv.writer(outfile)
    csvw.writerow(["aglomerado", "estado", "cidade", "codigo_ibge"])
    for aglomerado_nome, aglomerado_cidades in aglomerados.items():
        for codigo, estado, nome_simple in aglomerado_cidades:
            csvw.writerow([aglomerado_nome, estado, nome_simple, codigo])

