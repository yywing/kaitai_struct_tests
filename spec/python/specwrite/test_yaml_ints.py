# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.yaml_ints import YamlInts

class TestYamlInts(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestYamlInts, self).__init__(*args, **kwargs)
        self.struct_class = YamlInts
        self.src_filename = 'src/fixed_struct.bin'

