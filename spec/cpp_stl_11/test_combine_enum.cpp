// Autogenerated from KST: please remove this line if doing any edits by hand!

#include <boost/test/unit_test.hpp>
#include "combine_enum.h"
#include <iostream>
#include <fstream>
#include <vector>

BOOST_AUTO_TEST_CASE(test_combine_enum) {
    std::ifstream ifs("src/enum_0.bin", std::ifstream::binary);
    kaitai::kstream ks(&ifs);
    combine_enum_t* r = new combine_enum_t(&ks);

    BOOST_CHECK_EQUAL(r->enum_u4(), combine_enum_t::ANIMAL_PIG);
    BOOST_CHECK_EQUAL(r->enum_u2(), combine_enum_t::ANIMAL_HORSE);
    BOOST_CHECK_EQUAL(r->enum_u4_u2(), combine_enum_t::ANIMAL_HORSE);

    delete r;
}
