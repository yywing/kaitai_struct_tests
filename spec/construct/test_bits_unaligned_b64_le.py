# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from bits_unaligned_b64_le import _schema

class TestBitsUnalignedB64Le(unittest.TestCase):
    def test_bits_unaligned_b64_le(self):
        r = _schema.parse_file('src/process_xor_4.bin')

        self.assertEqual(r.a, False)
        self.assertEqual(r.b, 1902324737369038326)
        self.assertEqual(r.c, 71)
