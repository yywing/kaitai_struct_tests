# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.switch_bytearray import SwitchBytearray

class TestSwitchBytearray(unittest.TestCase):
    def test_switch_bytearray(self):
        with SwitchBytearray.from_file('src/switch_opcodes.bin') as r:

            self.assertEqual(len(r.opcodes), 4)
            self.assertEqual(r.opcodes[0].code, b"\x53")
            self.assertEqual(r.opcodes[0].body.value, u"foobar")
            self.assertEqual(r.opcodes[1].code, b"\x49")
            self.assertEqual(r.opcodes[1].body.value, 66)
            self.assertEqual(r.opcodes[2].code, b"\x49")
            self.assertEqual(r.opcodes[2].body.value, 55)
            self.assertEqual(r.opcodes[3].code, b"\x53")
            self.assertEqual(r.opcodes[3].body.value, u"")
