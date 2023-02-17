# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from expr_if_int_eq import ExprIfIntEq

class TestExprIfIntEq(unittest.TestCase):
    def test_expr_if_int_eq(self):
        with ExprIfIntEq.from_file('src/process_coerce_switch.bin') as r:

            self.assertEqual(r.seq_eq_lit, True)
            self.assertEqual(r.seq_eq_calc, True)
            self.assertEqual(r.seq_eq_calc_if, True)
            self.assertEqual(r.seq_eq_seq_if, True)
            self.assertEqual(r.calc_eq_lit, True)
            self.assertEqual(r.calc_eq_calc_if, True)
            self.assertEqual(r.calc_eq_seq_if, True)
            self.assertEqual(r.calc_if_eq_lit, True)
            self.assertEqual(r.calc_if_eq_seq_if, True)
            self.assertEqual(r.seq_if_eq_lit, True)
