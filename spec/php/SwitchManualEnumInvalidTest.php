<?php
// Autogenerated from KST: please remove this line if doing any edits by hand!

namespace Kaitai\Struct\Tests;

class SwitchManualEnumInvalidTest extends TestCase {
    public function testSwitchManualEnumInvalid() {
        $r = SwitchManualEnumInvalid::fromFile(self::SRC_DIR_PATH . '/enum_negative.bin');

        $this->assertSame(2, count($r->opcodes()));
        $this->assertSame(255, $r->opcodes()[0]->code());
        $this->assertNull($r->opcodes()[0]->body());
        $this->assertSame(1, $r->opcodes()[1]->code());
        $this->assertNull($r->opcodes()[1]->body());
    }
}
