# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest
from specwrite.common_spec import CommonSpec

from testwrite.instance_io_user_earlier import InstanceIoUserEarlier

class TestInstanceIoUserEarlier(CommonSpec.Base):
    def __init__(self, *args, **kwargs):
        super(TestInstanceIoUserEarlier, self).__init__(*args, **kwargs)
        self.struct_class = InstanceIoUserEarlier
        self.src_filename = 'src/switch_opcodes2.bin'
