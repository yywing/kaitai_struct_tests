local luaunit = require("luaunit")

require("imports_abs_rel")

TestImportsAbsRel = {}

function TestImportsAbsRel:test_imports_abs_rel()
    local r = ImportsAbsRel:from_file("src/fixed_struct.bin")

    luaunit.assertEquals(r.one, 80)
    luaunit.assertEquals(r.two.one, 65)
    luaunit.assertEquals(r.two.two.one, 67)
end
