# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.debug_array_user import DebugArrayUser

class TestDebugArrayUser(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestDebugArrayUser, self).__init__(*args, **kwargs)
        self.struct_class = DebugArrayUser
        self.src_filename = 'src/fixed_struct.bin'
