# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.buffered_struct import BufferedStruct

class TestBufferedStruct(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestBufferedStruct, self).__init__(*args, **kwargs)
        self.struct_class = BufferedStruct
        self.src_filename = 'src/buffered_struct.bin'

