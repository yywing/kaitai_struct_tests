<?php
// Autogenerated from KST: please remove this line if doing any edits by hand!

namespace Kaitai\Struct\Tests;

class InstanceIoUserTest extends TestCase {
    public function testInstanceIoUser() {
        $r = InstanceIoUser::fromFile(self::SRC_DIR_PATH . '/instance_io.bin');

        $this->assertSame(3, $r->qtyEntries());
        $this->assertSame("the", $r->entries()[0]->name());
        $this->assertSame("rainy", $r->entries()[1]->name());
        $this->assertSame("day it is", $r->entries()[2]->name());
    }
}
