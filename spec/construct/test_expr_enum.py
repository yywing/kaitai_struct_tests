# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from expr_enum import _schema

class TestExprEnum(unittest.TestCase):
    def test_expr_enum(self):
        r = _schema.parse_file('src/term_strz.bin')

        self.assertEqual(r.const_dog, 'dog')
        self.assertEqual(r.derived_boom, 'boom')
        self.assertEqual(r.derived_dog, 'dog')
