# Autogenerated from KST: please remove this line if doing any edits by hand!

import unittest

from process_bytes_pad_term import ProcessBytesPadTerm

class TestProcessBytesPadTerm(unittest.TestCase):
    def test_process_bytes_pad_term(self):
        with ProcessBytesPadTerm.from_file('src/str_pad_term.bin') as r:

            self.assertEqual(r.str_pad, b"\x66\x61\x67\x24")
            self.assertEqual(r.str_term, b"\x66\x61\x67\x27\x73\x7A\x7A")
            self.assertEqual(r.str_term_and_pad, b"\x66\x61\x67\x3E\x3E\x3E\x26\x77\x74\x67\x3E\x3E\x3E")
            self.assertEqual(r.str_term_include, b"\x66\x61\x67\x21\x77\x74\x6F\x55")
