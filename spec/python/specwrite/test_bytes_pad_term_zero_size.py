# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.bytes_pad_term_zero_size import BytesPadTermZeroSize

class TestBytesPadTermZeroSize(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestBytesPadTermZeroSize, self).__init__(*args, **kwargs)
        self.struct_class = BytesPadTermZeroSize
        self.src_filename = 'src/enum_negative.bin'

