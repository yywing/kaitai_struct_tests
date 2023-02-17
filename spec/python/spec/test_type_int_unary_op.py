# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.type_int_unary_op import TypeIntUnaryOp

class TestTypeIntUnaryOp(unittest.TestCase):
    def test_type_int_unary_op(self):
        with TypeIntUnaryOp.from_file('src/fixed_struct.bin') as r:

            self.assertEqual(r.value_s2, 16720)
            self.assertEqual(r.value_s8, 4706543082108963651)
            self.assertEqual(r.unary_s2, -16720)
            self.assertEqual(r.unary_s8, -4706543082108963651)
