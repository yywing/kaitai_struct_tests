// Autogenerated from KST: please remove this line if doing any edits by hand!

#include <boost/test/unit_test.hpp>
#include "zlib_with_header_78.h"
#include <iostream>
#include <fstream>
#include <vector>

BOOST_AUTO_TEST_CASE(test_zlib_with_header_78) {
    std::ifstream ifs("src/zlib_with_header_78.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    zlib_with_header_78_t* r = new zlib_with_header_78_t(&ks);

    BOOST_CHECK_EQUAL(r->data(), std::string("\x61\x20\x71\x75\x69\x63\x6B\x20\x62\x72\x6F\x77\x6E\x20\x66\x6F\x78\x20\x6A\x75\x6D\x70\x73\x20\x6F\x76\x65\x72", 28));

    delete r;
}
