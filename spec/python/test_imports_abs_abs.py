import unittest

from imports_abs_abs import ImportsAbsAbs

class TestImportsAbsAbs(unittest.TestCase):
    def test_imports_abs_abs(self):
        with ImportsAbsAbs.from_file('src/fixed_struct.bin') as r:

            self.assertEqual(r.one, 80)
            self.assertEqual(r.two.one, 65)
            self.assertEqual(r.two.two.one, 67)
