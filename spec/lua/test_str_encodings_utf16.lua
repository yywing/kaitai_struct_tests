-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("str_encodings_utf16")

TestStrEncodingsUtf16 = {}

function TestStrEncodingsUtf16:test_str_encodings_utf16()
    local r = StrEncodingsUtf16:from_file("src/str_encodings_utf16.bin")

    luaunit.assertEquals(r.len_be, 12)
    luaunit.assertEquals(r.be_bom_removed.bom, 65279)
    luaunit.assertEquals(r.be_bom_removed.str, "\u{3053}\u{3093}\u{306b}\u{3061}\u{306f}")
    luaunit.assertEquals(r.len_le, 12)
    luaunit.assertEquals(r.le_bom_removed.bom, 65279)
    luaunit.assertEquals(r.le_bom_removed.str, "\u{3053}\u{3093}\u{306b}\u{3061}\u{306f}")
end
