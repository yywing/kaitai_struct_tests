# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.valid_fail_eq_str import ValidFailEqStr

class TestValidFailEqStr(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestValidFailEqStr, self).__init__(*args, **kwargs)
        self.struct_class = ValidFailEqStr
        self.src_filename = 'src/fixed_struct.bin'

    def test_read_write_roundtrip(self):
        self.skipTest("cannot use roundtrip because parsing is expected to fail")
