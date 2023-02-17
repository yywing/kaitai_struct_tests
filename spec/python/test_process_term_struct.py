# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from process_term_struct import ProcessTermStruct

class TestProcessTermStruct(unittest.TestCase):
    def test_process_term_struct(self):
        with ProcessTermStruct.from_file('src/term_strz.bin') as r:

            self.assertEqual(r.s1.value, b"\x46\x4F\x4F")
            self.assertEqual(r.s2.value, b"\x42\x41\x52")
            self.assertEqual(r.s3.value, b"\x5C\x42\x41\x5A\x20")
