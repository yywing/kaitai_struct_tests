# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.process_term_struct import ProcessTermStruct

class TestProcessTermStruct(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestProcessTermStruct, self).__init__(*args, **kwargs)
        self.struct_class = ProcessTermStruct
        self.src_filename = 'src/term_strz.bin'

