# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.enum_int_range_s import EnumIntRangeS

class TestEnumIntRangeS(unittest.TestCase):
    def test_enum_int_range_s(self):
        with EnumIntRangeS.from_file('src/enum_int_range_s.bin') as r:

            self.assertEqual(r.f1, EnumIntRangeS.Constants.int_min)
            self.assertEqual(r.f2, EnumIntRangeS.Constants.zero)
            self.assertEqual(r.f3, EnumIntRangeS.Constants.int_max)
