-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("type_ternary_2nd_falsy")

TestTypeTernary2ndFalsy = {}

function TestTypeTernary2ndFalsy:test_type_ternary_2nd_falsy()
    local r = TypeTernary2ndFalsy:from_file("src/switch_integers.bin")

    luaunit.assertEquals(r.v_false, false)
    luaunit.assertEquals(r.v_int_zero, 0)
    luaunit.assertEquals(r.v_int_neg_zero, 0)
    luaunit.assertAlmostEquals(r.v_float_zero, 0.0, 0.000001)
    luaunit.assertAlmostEquals(r.v_float_neg_zero, -0.0, 0.000001)
    luaunit.assertEquals(r.v_str_w_zero, "0")
    luaunit.assertEquals(string.len(r.v_str_w_zero), 1)
    luaunit.assertEquals(r.ut.m, 7)
    luaunit.assertNil(r.v_null_ut)
    luaunit.assertEquals(r.v_str_empty, "")
    luaunit.assertEquals(string.len(r.v_str_empty), 0)
    luaunit.assertEquals(#r.int_array, 2)
    luaunit.assertEquals(#r.v_int_array_empty, 0)
end
