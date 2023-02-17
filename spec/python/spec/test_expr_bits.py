# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.expr_bits import ExprBits

class TestExprBits(unittest.TestCase):
    def test_expr_bits(self):
        with ExprBits.from_file('src/switch_opcodes.bin') as r:

            self.assertEqual(r.a, 2)
            self.assertEqual(r.enum_seq, ExprBits.Items.foo)
            self.assertEqual(r.byte_size, b"\x66\x6F")
            self.assertEqual(len(r.repeat_expr), 2)
            self.assertEqual(r.repeat_expr[0], 111)
            self.assertEqual(r.repeat_expr[1], 98)
            self.assertEqual(r.switch_on_type, 97)
            self.assertEqual(r.switch_on_endian.foo, 29184)
            self.assertEqual(r.enum_inst, ExprBits.Items.bar)
            self.assertEqual(r.inst_pos, 111)
