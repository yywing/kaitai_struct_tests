# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.bits_unaligned_b32_be import BitsUnalignedB32Be

class TestBitsUnalignedB32Be(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestBitsUnalignedB32Be, self).__init__(*args, **kwargs)
        self.struct_class = BitsUnalignedB32Be
        self.src_filename = 'src/process_xor_4.bin'

