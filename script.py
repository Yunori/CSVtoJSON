#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:33:52 2017

@author: Yunori
"""
import json
import pandas as pd

def parsecsv(dpts, dataset):
    """Parse un csv et renvoie un dictionnaire trié."""

    tailledpt = len(dpts)
    counter1 = 0
    listedpts = {}

    while counter1 < tailledpt:
        listedpts[dpts.iloc[counter1, 1]] = dpts.iloc[counter1, 2]
        counter1 += 1

    tailledata = len(dataset)
    counter2 = 0
    final = {}

    while counter2 < tailledata:
        codepostal = str(dataset.iloc[counter2, 0])

        if codepostal[:2] == '97' or codepostal[:2] == '98':
            codedpt = str(dataset.iloc[counter2, 0])[:3]
        else:
            codedpt = str(dataset.iloc[counter2, 0])[:2]
        if codedpt == '20':
            codedpt = '2a'
        elif codedpt == '21':
            codedpt = '2b'
        elif codepostal == '42620':
            codedpt = '03'
        elif codepostal == '05110':
            codedpt = '04'
        elif codepostal == '33220':
            codedpt = '24'

        nomdpt = listedpts[codedpt]
        nomville = dataset.iloc[counter2, 1]
        adresse = dataset.iloc[counter2, 2]

        if nomdpt not in final:
            final[nomdpt] = {}
        if nomville not in final[nomdpt]:
            final[nomdpt][nomville] = {}
        final[nomdpt][nomville] = {1:{}}
        indecounter1 = len(final[nomdpt][nomville])
        final[nomdpt][nomville][indecounter1] = {}
        final[nomdpt][nomville][indecounter1]['codepostal'] = codepostal
        final[nomdpt][nomville][indecounter1]['departement'] = nomdpt
        final[nomdpt][nomville][indecounter1]['ville'] = nomville
        final[nomdpt][nomville][indecounter1]['adresse'] = adresse
        counter2 += 1

    return final


with open('data.txt', 'w') as outfile:
    json.dump(parsecsv(pd.read_csv('Departements.csv'), pd.read_csv('Dataset.csv')), outfile)
