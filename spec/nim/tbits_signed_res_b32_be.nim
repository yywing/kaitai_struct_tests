# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/bits_signed_res_b32_be
import auxiliary/test_utils

let r = BitsSignedResB32Be.fromFile("../../src/bits_shift_by_b32_le.bin")

assert r.a == 4294967295'i64
