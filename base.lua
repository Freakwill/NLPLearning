#!/usr/bin/env lua

function contains(t, a)
    for i, b in ipairs(t) do
        if b == a then
            return true
        end
    end
    return false
end

function filter(t, key)
    new = {}
    for i, b in ipairs(t) do
        if key(b) then
            table.insert(new, #new+1, b)
        end
    end
    return new
end

local function iter(t, i)
    -- State index value
    i = i + 1
    local v = t[i]
    if v then
        return v
    end
end

function items(t)
    -- iter function, initial value
    return iter, t, 0
end
