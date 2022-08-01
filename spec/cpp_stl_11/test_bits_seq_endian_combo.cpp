// Autogenerated from KST: please remove this line if doing any edits by hand!

#include <boost/test/unit_test.hpp>
#include "bits_seq_endian_combo.h"
#include <iostream>
#include <fstream>
#include <vector>

BOOST_AUTO_TEST_CASE(test_bits_seq_endian_combo) {
    std::ifstream ifs("src/process_xor_4.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    bits_seq_endian_combo_t* r = new bits_seq_endian_combo_t(&ks);

    BOOST_CHECK_EQUAL(r->be1(), 59);
    BOOST_CHECK_EQUAL(r->be2(), 187);
    BOOST_CHECK_EQUAL(r->le3(), 163);
    BOOST_CHECK_EQUAL(r->be4(), 20);
    BOOST_CHECK_EQUAL(r->le5(), 10);
    BOOST_CHECK_EQUAL(r->le6(), 36);
    BOOST_CHECK_EQUAL(r->le7(), 26);
    BOOST_CHECK_EQUAL(r->be8(), true);

    delete r;
}
