# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from testformats.enum_to_i_class_border_1 import EnumToIClassBorder1

class TestEnumToIClassBorder1(unittest.TestCase):
    def test_enum_to_i_class_border_1(self):
        with EnumToIClassBorder1.from_file('src/enum_0.bin') as r:

            self.assertEqual(r.pet_1, EnumToIClassBorder1.Animal.cat)
            self.assertEqual(r.pet_2, EnumToIClassBorder1.Animal.chicken)
            self.assertEqual(r.checker.is_dog, True)
