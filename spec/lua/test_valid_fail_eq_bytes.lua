-- Autogenerated from KST: please remove this line if doing any edits by hand!

local luaunit = require("luaunit")

require("valid_fail_eq_bytes")

TestValidFailEqBytes = {}

function TestValidFailEqBytes:test_valid_fail_eq_bytes()
    luaunit.assertErrorMsgMatches(".+: not equal, expected .*, but got .*", ValidFailEqBytes.from_file, ValidFailEqBytes, "src/fixed_struct.bin")
end
