# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.type_ternary import TypeTernary

class TestTypeTernary(unittest.TestCase):
    def test_type_ternary(self):
        with TypeTernary.from_file('src/term_strz.bin') as r:

            self.assertEqual(r.dif.value, 101)
