// Autogenerated from KST: please remove this line if doing any edits by hand!

#include <boost/test/unit_test.hpp>
#include "bits_signed_shift_b64_le.h"
#include <iostream>
#include <fstream>
#include <vector>

BOOST_AUTO_TEST_CASE(test_bits_signed_shift_b64_le) {
    std::ifstream ifs("src/bits_signed_shift_b64_le.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    bits_signed_shift_b64_le_t* r = new bits_signed_shift_b64_le_t(&ks);

    BOOST_CHECK_EQUAL(r->a(), 0);
    BOOST_CHECK_EQUAL(r->b(), 255);

    delete r;
}
