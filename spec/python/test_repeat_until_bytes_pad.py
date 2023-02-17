# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from repeat_until_bytes_pad import RepeatUntilBytesPad

class TestRepeatUntilBytesPad(unittest.TestCase):
    def test_repeat_until_bytes_pad(self):
        with RepeatUntilBytesPad.from_file('src/repeat_until_process.bin') as r:

            self.assertEqual(len(r.records), 3)
            self.assertEqual(r.records[0], b"\xE8\xBA")
            self.assertEqual(r.records[1], b"\xFA\x9E\xB8")
            self.assertEqual(r.records[2], b"\xAA\x55\x55\x55\x55")
