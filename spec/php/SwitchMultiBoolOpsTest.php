<?php
namespace Kaitai\Struct\Tests;

class SwitchMultiBoolOpsTest extends TestCase {
    public function testSwitchMultiBoolOps() {
        $r = SwitchMultiBoolOps::fromFile(self::SRC_DIR_PATH . "/switch_integers.bin");

        $this->assertSame(4, count($r->opcodes));

        $this->assertSame(1, $r->opcodes[0]->code);
        $this->assertSame(7, $r->opcodes[0]->body);

        $this->assertSame(2, $r->opcodes[1]->code);
        $this->assertSame(0x4040, $r->opcodes[1]->body);

        $this->assertSame(4, $r->opcodes[2]->code);
        $this->assertSame(4919, $r->opcodes[2]->body);

        $this->assertSame(8, $r->opcodes[3]->code);
        $this->assertSame(4919, $r->opcodes[3]->body);
    }
}
