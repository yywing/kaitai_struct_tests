<?php
// Autogenerated from KST: please remove this line if doing any edits by hand!

namespace Kaitai\Struct\Tests;

class PositionAbsTest extends TestCase {
    public function testPositionAbs() {
        $r = PositionAbs::fromFile(self::SRC_DIR_PATH . '/position_abs.bin');

        $this->assertSame(32, $r->indexOffset());
        $this->assertSame("foo", $r->index()->entry());
    }
}
