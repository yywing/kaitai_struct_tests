// Autogenerated from KST: please remove this line if doing any edits by hand!

package io.kaitai.struct.specwrite;

import io.kaitai.struct.KaitaiStruct.ReadWrite;
import io.kaitai.struct.testwrite.ValidFailRangeStr;
import org.testng.annotations.Test;
import org.testng.SkipException;

public class TestValidFailRangeStr extends CommonSpec {
    @Override
    protected Class<? extends ReadWrite> getStructClass() {
        return ValidFailRangeStr.class;
    }

    @Override
    protected String getSrcFilename() {
        return "fixed_struct.bin";
    }

    @Override
    @Test
    protected void testReadWriteRoundtrip() throws Exception {
        throw new SkipException("cannot use roundtrip because parsing is expected to fail");
    }
}
