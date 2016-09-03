<?php
namespace Kaitai\Struct\Tests;

class TermStrzTest extends TestCase {
    public function testTermStrz() {
        $r = TermStrz::fromFile(self::SRC_DIR_PATH . "/term_strz.bin");

        $this->assertEquals("foo", $r->s1());
        $this->assertEquals("bar", $r->s2());
        $this->assertEquals("|baz@", $r->s3());
    }
}
