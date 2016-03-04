import unittest

from expr_2 import Expr2

class TestExpr2(unittest.TestCase):
    def test_expr_2(self):
        r = Expr2.from_file("src/str_encodings.bin")

        self.assertEquals(r.str1.len_orig, 10)
        self.assertEquals(r.str1.len_mod, 7)
        self.assertEquals(r.str1.str, "Some AS")

        self.assertEquals(r.str1_len, 7)
        self.assertEquals(r.str1_len_mod, 7)
        self.assertEquals(r.str1_byte1, 0x49)
        self.assertEquals(r.str1_avg, 0x49)
        self.assertEquals(r.str1_char5, "e")

        self.assertEquals(r.str1_tuple5.byte0, 0x65)
        self.assertEquals(r.str1_tuple5.byte1, 0x20)
        self.assertEquals(r.str1_tuple5.byte2, 0x41)
        self.assertEquals(r.str1_tuple5.avg, 0x30)

        self.assertEquals(r.str2_tuple5.byte0, 0x65)
        self.assertEquals(r.str2_tuple5.byte1, 0x20)
        self.assertEquals(r.str2_tuple5.byte2, 0x41)
        self.assertEquals(r.str2_tuple5.avg, 0x30)
