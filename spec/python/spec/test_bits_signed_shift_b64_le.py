# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.bits_signed_shift_b64_le import BitsSignedShiftB64Le

class TestBitsSignedShiftB64Le(unittest.TestCase):
    def test_bits_signed_shift_b64_le(self):
        with BitsSignedShiftB64Le.from_file('src/bits_signed_shift_b64_le.bin') as r:

            self.assertEqual(r.a, 0)
            self.assertEqual(r.b, 255)
