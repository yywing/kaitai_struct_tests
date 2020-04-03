# Autogenerated from KST: please remove this line if doing any edits by hand!

import os, streams, options, sequtils, unittest
import ../../../compiled/nim/switch_manual_enum_invalid
import ../test_utils

let r = SwitchManualEnumInvalid.fromFile("src/enum_negative.bin")

test "SwitchManualEnumInvalid":

  check(len(r.opcodes) == int(2))
  check(r.opcodes[0].code == SwitchManualEnumInvalid_Opcode_CodeEnum(255))
  check(r.opcodes[0].body == nil)
  check(r.opcodes[1].code == SwitchManualEnumInvalid_Opcode_CodeEnum(1))
  check(r.opcodes[1].body == nil)
  discard
