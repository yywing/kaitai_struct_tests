# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.process_coerce_usertype2 import ProcessCoerceUsertype2

class TestProcessCoerceUsertype2(unittest.TestCase):
    def test_process_coerce_usertype2(self):
        with ProcessCoerceUsertype2.from_file('src/process_coerce_bytes.bin') as r:

            self.assertEqual(r.records[0].flag, 0)
            self.assertEqual(r.records[0].buf.value, 1094795585)
            self.assertEqual(r.records[1].flag, 1)
            self.assertEqual(r.records[1].buf.value, 1111638594)
