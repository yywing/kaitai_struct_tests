# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.valid_fail_range_float import ValidFailRangeFloat

class TestValidFailRangeFloat(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestValidFailRangeFloat, self).__init__(*args, **kwargs)
        self.struct_class = ValidFailRangeFloat
        self.src_filename = 'src/floating_points.bin'

    def test_read_write_roundtrip(self):
        self.skipTest("cannot use roundtrip because parsing is expected to fail")
