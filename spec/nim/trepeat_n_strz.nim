# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/repeat_n_strz
import auxiliary/test_utils

let r = RepeatNStrz.fromFile("../../src/repeat_n_strz.bin")

assert r.qty == 2
assert r.lines == @[string("foo"), "bar"]
