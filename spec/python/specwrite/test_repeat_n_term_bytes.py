# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.repeat_n_term_bytes import RepeatNTermBytes

class TestRepeatNTermBytes(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestRepeatNTermBytes, self).__init__(*args, **kwargs)
        self.struct_class = RepeatNTermBytes
        self.src_filename = 'src/repeat_until_process.bin'
