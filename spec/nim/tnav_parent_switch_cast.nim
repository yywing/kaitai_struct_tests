# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils
import ../../compiled/nim/nav_parent_switch_cast
import auxiliary/test_utils

let r = NavParentSwitchCast.fromFile("../../src/switch_integers.bin")

assert r.main.bufType == 1
assert r.main.flag == 7
assert (NavParentSwitchCast_Foo_One(r.main.buf)).branch.flag == 7
