# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/expr_str_encodings
import auxiliary/test_utils

let r = ExprStrEncodings.fromFile("../../src/str_encodings.bin")

assert r.str1Eq == true
assert r.str2Eq == true
assert r.str3Eq == true
assert r.str3EqStr2 == true
assert r.str4Eq == true
assert r.str4GtStrCalc == true
assert r.str4GtStrFromBytes == true
