// Autogenerated from KST: please remove this line if doing any edits by hand!

package io.kaitai.struct.specwrite;

import io.kaitai.struct.KaitaiStruct.ReadWrite;
import io.kaitai.struct.testwrite.CastNested;
import org.testng.annotations.Test;

public class TestCastNested extends CommonSpec {
    @Override
    protected Class<? extends ReadWrite> getStructClass() {
        return CastNested.class;
    }

    @Override
    protected String getSrcFilename() {
        return "switch_opcodes.bin";
    }

}
