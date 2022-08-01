# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from switch_manual_enum_invalid import _schema

class TestSwitchManualEnumInvalid(unittest.TestCase):
    def test_switch_manual_enum_invalid(self):
        r = _schema.parse_file('src/enum_negative.bin')

        self.assertEqual(len(r.opcodes), 2)
        self.assertEqual(r.opcodes[0].code, 255)
        self.assertIsNone(r.opcodes[0].body)
        self.assertEqual(r.opcodes[1].code, 1)
        self.assertIsNone(r.opcodes[1].body)
