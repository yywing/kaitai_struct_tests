-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("bits_signed_res_b32_be")

TestBitsSignedResB32Be = {}

function TestBitsSignedResB32Be:test_bits_signed_res_b32_be()
    local r = BitsSignedResB32Be:from_file("src/bits_shift_by_b32_le.bin")

    luaunit.assertEquals(r.a, 4294967295)
end
