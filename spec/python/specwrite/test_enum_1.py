# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.enum_1 import Enum1

class TestEnum1(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestEnum1, self).__init__(*args, **kwargs)
        self.struct_class = Enum1
        self.src_filename = 'src/enum_0.bin'
