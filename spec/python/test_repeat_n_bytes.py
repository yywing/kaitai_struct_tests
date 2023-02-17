# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from repeat_n_bytes import RepeatNBytes

class TestRepeatNBytes(unittest.TestCase):
    def test_repeat_n_bytes(self):
        with RepeatNBytes.from_file('src/repeat_until_process.bin') as r:

            self.assertEqual(len(r.records), 3)
            self.assertEqual(r.records[0], b"\xE8\xBA\xAA\xAA\xAA")
            self.assertEqual(r.records[1], b"\xFA\x9E\xB8\xAA\xAA")
            self.assertEqual(r.records[2], b"\xAA\x55\x55\x55\x55")
