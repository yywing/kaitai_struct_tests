# Autogenerated from KST: please remove this line if doing any edits by hand!

package spec::perl::TestValidShort;

use strict;
use warnings;
use base qw(Test::Class);
use Test::More;
use ValidShort;

sub test_valid_short: Test(0) {
    my $r = ValidShort->from_file('src/fixed_struct.bin');

}

Test::Class->runtests;
