# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
import kaitaistruct

from valid_fail_max_int import ValidFailMaxInt

class TestValidFailMaxInt(unittest.TestCase):
    def test_valid_fail_max_int(self):
        with self.assertRaises(kaitaistruct.ValidationGreaterThanError):
            with ValidFailMaxInt.from_file('src/fixed_struct.bin') as r:
                pass
