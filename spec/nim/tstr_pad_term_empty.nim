# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/str_pad_term_empty
import auxiliary/test_utils

let r = StrPadTermEmpty.fromFile("../../src/str_pad_term_empty.bin")

assert r.strPad == ""
assert r.strTerm == ""
assert r.strTermAndPad == ""
assert r.strTermInclude == "@"
