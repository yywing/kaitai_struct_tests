# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/bits_signed_shift_b32_le
import auxiliary/test_utils

let r = BitsSignedShiftB32Le.fromFile("../../src/bits_signed_shift_b32_le.bin")

assert r.a == 0
assert r.b == 255
