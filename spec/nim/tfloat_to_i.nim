# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/float_to_i
import auxiliary/test_utils

let r = FloatToI.fromFile("../../src/floating_points.bin")

assert r.singleValue == 0.5
assert r.doubleValue == 0.25
assert r.singleI == 0
assert r.doubleI == 0
assert r.float1I == 1
assert r.float2I == 1
assert r.float3I == 1
assert r.float4I == -2
