# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/process_custom_no_args
import auxiliary/test_utils

let r = ProcessCustomNoArgs.fromFile("../../src/process_rotate.bin")

assert r.buf == @[95'u8, 9'u8, 172'u8, 141'u8, 141'u8, 237'u8, 95'u8]
