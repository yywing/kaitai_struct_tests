// Autogenerated from KST: please remove this line if doing any edits by hand!

package io.kaitai.struct.spec;

import io.kaitai.struct.testformats.ExprStrOps;
import org.testng.annotations.Test;
import static org.testng.Assert.*;
public class TestExprStrOps extends CommonSpec {

    @Test
    public void testExprStrOps() throws Exception {
        ExprStrOps r = ExprStrOps.fromFile(SRC_DIR + "term_strz.bin");

        assertEquals(r.one(), "foo|b");
        assertIntEquals(r.oneLen(), 5);
        assertEquals(r.oneRev(), "b|oof");
        assertEquals(r.oneSubstr0To3(), "foo");
        assertEquals(r.oneSubstr2To5(), "o|b");
        assertEquals(r.oneSubstr3To3(), "");
        assertEquals(r.two(), "0123456789");
        assertIntEquals(r.twoLen(), 10);
        assertEquals(r.twoRev(), "9876543210");
        assertEquals(r.twoSubstr0To7(), "0123456");
        assertEquals(r.twoSubstr4To10(), "456789");
        assertEquals(r.twoSubstr0To10(), "0123456789");
        assertIntEquals(r.toIAttr(), 9173);
        assertIntEquals(r.toIR10(), -72);
        assertIntEquals(r.toIR2(), 86);
        assertIntEquals(r.toIR8(), 465);
        assertIntEquals(r.toIR16(), 18383);
    }
}
