# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.nested_same_name import NestedSameName

class TestNestedSameName(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestNestedSameName, self).__init__(*args, **kwargs)
        self.struct_class = NestedSameName
        self.src_filename = 'src/repeat_n_struct.bin'

