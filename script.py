#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:33:52 2017

@author: Yunori
"""
import json
import pandas as pd

dataset = pd.read_csv('Dataset.csv', dtype=object, encoding='cp850')
dpts = pd.read_csv('Departements.csv', dtype=object, encoding='utf_8')
dataset = dataset.sort_index(1, ascending=False)

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
    codepostal = str(dataset.iloc[counter2, 1])

    if codepostal[:2] == '97' or codepostal[:2] == '98' or codepostal[:2] == '20':
        codedpt = codepostal[:3]
    else:
        codedpt = codepostal[:2]
    if codedpt[:2] == '20':
        if codedpt == '202':
            codedpt = '2b'
        else:
            codedpt = '2a'
    elif codepostal == '42620':
        codedpt = '03'
    elif codepostal == '05110':
        codedpt = '04'
    elif codepostal == '33220':
        codedpt = '24'

    nomdpt = listedpts[codedpt]
    nomville = dataset.iloc[counter2, 0]
    adresse = dataset.iloc[counter2, 2]

    if nomdpt not in final:
        final[nomdpt] = {}
    if nomville not in final[nomdpt]:
        final[nomdpt][nomville] = {}
    indexcounter1 = len(final[nomdpt][nomville])
    final[nomdpt][nomville][indexcounter1] = {}
    final[nomdpt][nomville][indexcounter1]['codepostal'] = codepostal
    final[nomdpt][nomville][indexcounter1]['departement'] = nomdpt
    final[nomdpt][nomville][indexcounter1]['ville'] = nomville
    final[nomdpt][nomville][indexcounter1]['adresse'] = adresse
    counter2 += 1

with open('data.json', 'w') as outfile:
    json.dump(final, outfile)
