# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.imports_circular_a import ImportsCircularA

class TestImportsCircularA(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestImportsCircularA, self).__init__(*args, **kwargs)
        self.struct_class = ImportsCircularA
        self.src_filename = 'src/fixed_struct.bin'

