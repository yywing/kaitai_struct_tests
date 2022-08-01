-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("params_pass_array_struct")

TestParamsPassArrayStruct = {}

function TestParamsPassArrayStruct:test_params_pass_array_struct()
    local r = ParamsPassArrayStruct:from_file("src/position_to_end.bin")

    luaunit.assertEquals(#r.pass_structs.structs, 2)
    luaunit.assertEquals(r.pass_structs.structs[0 + 1].f, 1)
    luaunit.assertEquals(r.pass_structs.structs[1 + 1].b, 2)
end
