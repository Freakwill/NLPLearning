#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inverse maximum matching method
simpler, faster, and more pythonic
"""


_dictionary = {'南京', '南京市', '南京市长', '市长', '长江', '长江大桥', '江大桥', '大桥', '桥'}

def imm(text, maxlen=4):
    # inverse maximum matching method
    dictionary = _dictionary
    result = []
    index = len(text)
    while index > 0:
        m = min((index, maxlen))
        # dictionary = {e for e in _dictionary if e.endswith(text[index-1])}  # for speeding up
        for size in range(m, 0, -1):
            piece = text[(index-size):index]
            if piece in dictionary:
                result.insert(0, piece)
                index -= size
                break
        else:
            index -= 1
    return result

result = imm('南京市长江大桥')
print(result)
