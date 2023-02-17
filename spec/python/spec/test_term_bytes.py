# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.term_bytes import TermBytes

class TestTermBytes(unittest.TestCase):
    def test_term_bytes(self):
        with TermBytes.from_file('src/term_strz.bin') as r:

            self.assertEqual(r.s1, b"\x66\x6F\x6F")
            self.assertEqual(r.s2, b"\x62\x61\x72")
            self.assertEqual(r.s3, b"\x7C\x62\x61\x7A\x40")
