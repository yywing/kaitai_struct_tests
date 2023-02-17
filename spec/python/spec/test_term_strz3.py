# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.term_strz3 import TermStrz3

class TestTermStrz3(unittest.TestCase):
    def test_term_strz3(self):
        with TermStrz3.from_file('src/term_strz.bin') as r:

            self.assertEqual(r.s1, u"foo")
            self.assertEqual(r.s2, u"|bar|baz")
            self.assertEqual(r.s3, u"")
