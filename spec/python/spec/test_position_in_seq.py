# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.position_in_seq import PositionInSeq

class TestPositionInSeq(unittest.TestCase):
    def test_position_in_seq(self):
        with PositionInSeq.from_file('src/position_in_seq.bin') as r:

            self.assertEqual(r.numbers, [(0 + 1), 2, 3])
