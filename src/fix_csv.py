#!/usr/bin/env python3

import csv
import json

OUTDIR = "./data"

INFILE_NAME = "{}/arranjos-raw.csv".format(OUTDIR)
OUTFILE_JSON = "{}/arranjos.json".format(OUTDIR)
OUTFILE_CSV = "{}/arranjos.csv".format(OUTDIR)

arranjos = {}

with open(INFILE_NAME, "r") as infile:
    csvr = csv.reader(infile)

    actual_rowtype = None
    last_rowtype = None

    arranjo_nome = None 

    for nome, codigo in csvr:

        actual_rowtype = "c" if codigo else "a"

        if actual_rowtype == "a":

            if last_rowtype == "c" or not last_rowtype:

                if last_rowtype == "c":
                    arranjos[arranjo_nome] = arranjo_cidades

                arranjo_nome = nome
                arranjo_cidades = []

            if last_rowtype == "a":

                arranjo_nome = "{} {}".format(arranjo_nome, nome)

        elif actual_rowtype == "c":
            nome_simple = nome[:-5]
            estado = nome[-3:-1]
            arranjo_cidades.append([codigo, estado, nome_simple])

        last_rowtype = actual_rowtype

arranjos[arranjo_nome] = arranjo_cidades

with open(OUTFILE_JSON, "w") as outfile:
    json.dump(arranjos, outfile)

with open(OUTFILE_CSV, "w") as outfile:
    csvw = csv.writer(outfile)
    csvw.writerow(["arranjo", "estado", "cidade", "codigo_ibge"])
    for arranjo_nome, arranjo_cidades in arranjos.items():
        for codigo, estado, nome_simple in arranjo_cidades:
            csvw.writerow([arranjo_nome, estado, nome_simple, codigo])

