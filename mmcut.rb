#!/usr/bin/env ruby
# -*- coding: utf-8 -*-

<<~DOC
Inverse maximum matching method
DOC


$dictionary = ['南京', '南京市', '南京市长', '市长', '长江', '长江大桥', '江大桥', '大桥', '桥']

def imm(text, maxlen=4)
    # inverse maximum matching method
    dictionary = $dictionary
    result = []
    index = text.length
    while index > 0
        size = [index, maxlen].min
        # dictionary = $dictionary.collect{|e| e if e[-1] == text[index-1] }  # for speeding up
        while size > 0
            piece = text[(index-size)...index]
            if dictionary.index(piece)
                result.insert(0, piece)
                index -= size - 1
                break
            end
            size -= 1
        end
        index -= 1
    end
    return result
end

result = imm('南京市长江大桥')
puts result
