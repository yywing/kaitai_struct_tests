# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.multiple_use import MultipleUse

class TestMultipleUse(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestMultipleUse, self).__init__(*args, **kwargs)
        self.struct_class = MultipleUse
        self.src_filename = 'src/position_abs.bin'

