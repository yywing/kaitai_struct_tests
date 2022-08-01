# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from switch_repeat_expr_invalid import _schema

class TestSwitchRepeatExprInvalid(unittest.TestCase):
    def test_switch_repeat_expr_invalid(self):
        r = _schema.parse_file('src/switch_tlv.bin')

        self.assertEqual(r.code, 17)
        self.assertEqual(r.size, 9)
        self.assertEqual(r.body[0], b"\x53\x74\x75\x66\x66\x00\x4D\x65\x00")
