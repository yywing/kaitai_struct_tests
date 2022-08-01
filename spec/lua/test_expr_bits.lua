-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("expr_bits")

TestExprBits = {}

function TestExprBits:test_expr_bits()
    local r = ExprBits:from_file("src/switch_opcodes.bin")

    luaunit.assertEquals(r.a, 2)
    luaunit.assertEquals(r.enum_seq, ExprBits.Items.foo)
    luaunit.assertEquals(r.byte_size, "\102\111")
    luaunit.assertEquals(#r.repeat_expr, 2)
    luaunit.assertEquals(r.repeat_expr[0 + 1], 111)
    luaunit.assertEquals(r.repeat_expr[1 + 1], 98)
    luaunit.assertEquals(r.switch_on_type, 97)
    luaunit.assertEquals(r.switch_on_endian.foo, 29184)
    luaunit.assertEquals(r.enum_inst, ExprBits.Items.bar)
    luaunit.assertEquals(r.inst_pos, 111)
end
