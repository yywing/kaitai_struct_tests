# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from expr_if_int_ops import ExprIfIntOps

class TestExprIfIntOps(unittest.TestCase):
    def test_expr_if_int_ops(self):
        with ExprIfIntOps.from_file('src/process_coerce_switch.bin') as r:

            self.assertEqual(r.is_eq_prim, True)
            self.assertEqual(r.is_eq_boxed, True)
