<?php
// Autogenerated from KST: please remove this line if doing any edits by hand!

namespace Kaitai\Struct\Tests;

class TypeIntUnaryOpTest extends TestCase {
    public function testTypeIntUnaryOp() {
        $r = TypeIntUnaryOp::fromFile(self::SRC_DIR_PATH . '/fixed_struct.bin');

        $this->assertSame(16720, $r->valueS2());
        $this->assertSame(4706543082108963651, $r->valueS8());
        $this->assertSame(-16720, $r->unaryS2());
        $this->assertSame(-4706543082108963651, $r->unaryS8());
    }
}
