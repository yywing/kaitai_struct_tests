# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/expr_bytes_cmp
import auxiliary/test_utils

let r = ExprBytesCmp.fromFile("../../src/fixed_struct.bin")

assert r.one == @[80'u8]
assert r.two == @[65'u8, 67'u8, 75'u8]
assert r.isEq == true
assert r.isNe == false
assert r.isLt == true
assert r.isGt == false
assert r.isLe == true
assert r.isGe == false
assert r.isLt2 == false
assert r.isGt2 == true
