# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.repeat_until_bytes_pad import RepeatUntilBytesPad

class TestRepeatUntilBytesPad(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestRepeatUntilBytesPad, self).__init__(*args, **kwargs)
        self.struct_class = RepeatUntilBytesPad
        self.src_filename = 'src/repeat_until_process.bin'
