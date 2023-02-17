# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from repeat_eos_term_struct import RepeatEosTermStruct

class TestRepeatEosTermStruct(unittest.TestCase):
    def test_repeat_eos_term_struct(self):
        with RepeatEosTermStruct.from_file('src/process_rotate.bin') as r:

            self.assertEqual(len(r.records), 2)
            self.assertEqual(r.records[0].value, b"\x09\xAC\x8D\x8D\xED\xBA\x7B\x93\x63\x23\x01\x2A\x34\xB2")
            self.assertEqual(r.records[1].value, b"\x39\xB2")
