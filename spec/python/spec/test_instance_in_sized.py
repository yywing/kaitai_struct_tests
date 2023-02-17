# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.instance_in_sized import InstanceInSized

class TestInstanceInSized(unittest.TestCase):
    def test_instance_in_sized(self):
        with InstanceInSized.from_file('src/process_rotate.bin') as r:

            self.assertEqual(r.cont.seq_sized.seq_f, 9)
            self.assertEqual(r.cont.seq_sized.inst_invoked, 172)
            self.assertEqual(r.cont.seq_sized.inst_unused_by_seq, b"\x8D\x8D")
            self.assertEqual(r.cont.seq_in_stream.seq_f, 237)
            self.assertEqual(r.cont.seq_in_stream.inst, b"\xBA\x7B\x93")
            self.assertEqual(r.cont.inst_in_stream.seq_f, 99)
            self.assertEqual(r.cont.inst_in_stream.inst, b"\x23\x01\x2A")
            self.assertEqual(r.cont.inst_sized.seq_f, 52)
            self.assertEqual(r.cont.inst_sized.inst_invoked, 178)
            self.assertEqual(r.cont.inst_sized.inst_unused_by_seq, b"\x39\xB2")
