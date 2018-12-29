#!/usr/bin/env lua

-- Inverse maximum matching method

base = require "base"

dictionary = {'南京', '南京市', '南京市长', '市长', '长江', '长江大桥', '江大桥', '大桥', '桥'}

function imm(text, maxlen)
    -- inverse maximum matching method
    result = {}
    index = #text // 3
    while index > 0 do
        size = math.min(index, maxlen)
        -- dictionary = filter(dictionary, e -> e[-1] == text[index-1])  # for speeding up
        while size > 0 do
            piece = string.sub(text, (index-size) * 3 + 1, index * 3)
            if contains(dictionary,  piece) then
                table.insert(result, 1, piece)
                index = index - (size - 1)
                break
            end
            size = size - 1
        end
        index = index - 1
    end
    return result
end

result = imm("南京市长江大桥", 4)
for _, a in i pairs(result) do
    print(a)
end
