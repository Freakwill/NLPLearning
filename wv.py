#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from gensim.models import word2vec

# input the path of corpus
PATH = pathlib.Path('~/Folders/mycorpus/xxqg').expanduser()

# 构建模型

def get_corpus():
    import jieba
    import jieba.posseg as pseg
    import logging
    jieba.setLogLevel(logging.INFO)

    import readany

    def cut_flag(s):
        words = pseg.cut(s)
        return [f'{word_flag.word}/{word_flag.flag}' if word_flag.flag in {'u', 'w', 'x', 'y', 'z', 'un', 'o', 'p', 'uj'}
        else word_flag.word for word_flag in words]

    s = readany.read(PATH)
    sentences = s.split() # list of sentences
    STOPWORDS = {'要', '把', '着', '了', '有', '没有', '也', '到', '的', '在', '都', '不','就', '地',
    '以', '等', '是', '为', '更', '这', '从', '对', '使', '又', '既', '不是', '和', '与', '这个', '各',
    '。', '，', '、', '；', '/', '《','》','—', '（','）'}
    corpus= [[w for w in cut_flag(s) if w.partition('/')[0] not in STOPWORDS] for s in sentences]
    return corpus


def train(model_path=pathlib.Path('mymodel'), flag=True):
    if model_path.exists() and flag:
        model=word2vec.Word2Vec.load('mymodel')
    else:
        corpus = get_corpus()
        model = word2vec.Word2Vec(corpus, min_count=5, workers=5, size=100, window=5)
        model.save('mymodel')
    return model

# 进行相关性比较
def similarity1(word='中国', topn=50):
    words = model.wv.most_similar(word, topn=topn)
    words = [word[0] for word in words] + [word]

    from sklearn.manifold import TSNE
    X_tsne = TSNE(n_components=2, learning_rate=100).fit_transform(model.wv[words])

    import matplotlib.pyplot as plt 
    import matplotlib
    matplotlib.rcParams['font.sans-serif'] = ['SimHei'] 
    matplotlib.rcParams['font.family']='sans-serif'
    matplotlib.rcParams['axes.unicode_minus']=False

    plt.figure(figsize=(12, 7))
    plt.scatter(X_tsne[:,0], X_tsne[:,1])

    for i, Xi in enumerate(X_tsne[:-1]):
        x=Xi[0]
        y=Xi[1]
        plt.text(x, y, words[i],size = 15)
    plt.text(X_tsne[-1,0], X_tsne[-1,1], words[-1], size=18, color='r')
    plt.title(f'中心词：{word}')
    plt.show()

def similarity2(a, b, c):
    words = model.wv.most_similar_cosmul(positive=[c, b], negative=[a],topn=100)
    print(f'{a}:{b} == {c}:{words[0][0]} ["{a}"之于"{b}"如同"{c}"之于"{words[0][0]}"]')

if __name__ == '__main__':
    model = train(flag=False)
    similarity2('制度', '公正', '国家')
    similarity2('制度', '完善', '思想')
    similarity2('人', '国家', '党员')
    similarity2('共产主义', '实现', '理想')
    similarity1(word='社会', topn=60)
