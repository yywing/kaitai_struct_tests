-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("bits_shift_by_b32_le")

TestBitsShiftByB32Le = {}

function TestBitsShiftByB32Le:test_bits_shift_by_b32_le()
    local r = BitsShiftByB32Le:from_file("src/bits_shift_by_b32_le.bin")

    luaunit.assertEquals(r.a, 4294967295)
    luaunit.assertEquals(r.b, 0)
end
