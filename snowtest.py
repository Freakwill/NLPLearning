# -*- coding: utf-8 -*-

def section(x):
    line = '-' * 8
    print(line, x, line)


from snownlp import SnowNLP

section('情感判断')
s = SnowNLP('你是散发恶臭的畜生')

print(s.words)

if s.sentiments > 0.65:
    print('夸奖')
elif s.sentiments < 0.35:
    print('羞辱')
else:
    print('中性')

print(s.pinyin)


section('文本分析')
s = SnowNLP('「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

print(s.han)           # '「繁体字」「繁体中文」的叫法在台湾亦很常见。'

text = '''
从短期来看，加息对黄金有害无益，也就是说，加息政策预期升温，或者直接实施，都将导致金价走势下行压力加大。但是，从更长的时间跨度来看，加息政策落地之后，黄金价格则未必承压。
具体来看，加息预期升温，到加息政策正式实施，将逐步提振美元，最终让美元涨势到达顶点。
　　也就是说，加息政策落地之后，美元的拐点就将出现，相应的，作为以美元计价的投资品，黄金价格下跌态势的拐点也就来临了。所以说美联储加息对于美元来说将会提升它们的价值，而对于黄金来说就是有害而无益了。
'''

s = SnowNLP(text)

print(s.keywords(3))   # ['美元', '加息', '黄金']

print(s.summary(3))    # ['加息对黄金有害无益', '加息政策预期升温', '到加息政策正式实施']

print(s.sentences)
print(s.words)

section('相似度')
s = SnowNLP([['这篇', '文章'], ['那篇', '论文'], ['这个']])
print(s.sim(['文章'])) # [0.4686473612532025, 0, 0]
