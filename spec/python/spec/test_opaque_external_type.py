# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.opaque_external_type import OpaqueExternalType

class TestOpaqueExternalType(unittest.TestCase):
    def test_opaque_external_type(self):
        with OpaqueExternalType.from_file('src/term_strz.bin') as r:

            self.assertEqual(r.hw.one, 102)
