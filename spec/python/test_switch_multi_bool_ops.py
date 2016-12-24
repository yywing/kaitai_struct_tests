import unittest

from switch_multi_bool_ops import SwitchMultiBoolOps

class TestSwitchMultiBoolOps(unittest.TestCase):
    def test_switch_multi_bool_ops(self):
        r = SwitchMultiBoolOps.from_file("src/switch_integers.bin")

        self.assertEqual(len(r.opcodes), 4)

        self.assertEqual(r.opcodes[0].code, 1)
        self.assertEqual(r.opcodes[0].body, 7)

        self.assertEqual(r.opcodes[1].code, 2)
        self.assertEqual(r.opcodes[1].body, 0x4040)

        self.assertEqual(r.opcodes[2].code, 4)
        self.assertEqual(r.opcodes[2].body, 4919)

        self.assertEqual(r.opcodes[3].code, 8)
        self.assertEqual(r.opcodes[3].body, 4919)
