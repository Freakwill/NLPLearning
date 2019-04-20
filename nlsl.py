#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Statistical Learning for NL
"""

import numpy as np
import pandas as pd
import nltk

corpus = [
'When I do count the clock that tells the time',
'And see the brave day sunk in hideous night',
'When I behold the violet past prime',
'And sable curls all silverd oer with white',
'When lofty trees I see barren of leaves',
'Which erst from heat did canopy the herd',
'And summers green, all girded up in sheaves',
'Born on the bier with white and bristly beard',
'Then of thy beauty do I question make',
'That thou among the wastes of time must go',
'Since sweets and beauties do themselves forsake',
'And die as fast as they see others grow',
'And nothing gainst Times scythe can make defence'
'Save breed, to brave him when he takes thee hence'
]

def freq(doc):
    fd = nltk.FreqDist(doc)
    L = len(doc)
    return {w:f/L for w, f in fd.items()}


def wordFrame(docs):
    fs = [freq(doc) for doc in docs]
    df=pd.DataFrame(fs)
    return df.fillna(0)

docs = [doc.lower().split() for doc in corpus]
wf = wordFrame(docs)

def LSA(docs, *args, **kwargs):
    wf=wordFrame(docs)
    from sklearn.decomposition import PCA
    pca = PCA(*args, **kwargs)
    pca.fit(wf)
    return pca

lsa=LSA(docs, n_components=2)
print(lsa.transform(wf))
print(lsa.components_)

