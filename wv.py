#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from gensim.models import word2vec

# input the path of corpus
PATH = pathlib.Path('~/Folders/mycorpus/xxqg').expanduser()

# 构建模型
model_path = pathlib.Path('mymodel')
if model_path.exists():
    model=word2vec.Word2Vec.load('mymodel')
else:
    import jieba
    import jieba.posseg as pseg
    import logging
    jieba.setLogLevel(logging.INFO)

    import readany
    s = readany.read(PATH)

    def cut_flag(s):  
        return [f'{word_flag.word}/{word_flag.flag}' for word_flag in words]

    
    sentences = s.split()

    # 切分词汇
    STOPWORDS = {'要', '把', '着', '了', '有', '没有', '也', '到', '的', '在', '都', '不','就',
    '以', '等', '是', '为', '更', '这', '从', '对', '使', '又', '既', '不是', '和', '与', '这个',
    '。', '，', '、', '；'}
    sentences= [[w for w in jieba.cut(s) if w not in STOPWORDS] for s in sentences]

    model = word2vec.Word2Vec(sentences, min_count=3, workers=4, size=100, window=5)
    model.save('mymodel')

# 进行相关性比较
word = '人民'
words = model.wv.most_similar(word, topn=50)
words = [word[0] for word in words] + [word]

from sklearn.manifold import TSNE
X_tsne = TSNE(n_components=2, learning_rate=100).fit_transform(model.wv[words])

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['simhei'] 
matplotlib.rcParams['font.family']='sans-serif'

plt.figure(figsize=(12, 7))
plt.scatter(X_tsne[:,0], X_tsne[:,1])

for i, Xi in enumerate(X_tsne[:-1]):
    x=Xi[0]
    y=Xi[1]
    plt.text(x, y, words[i],size = 16)
plt.text(X_tsne[-1,0], X_tsne[-1,1], words[-1], size=18, color='r')
plt.title(f'中心词：{word}')
plt.show()
