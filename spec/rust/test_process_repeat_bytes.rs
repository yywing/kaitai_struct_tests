// Autogenerated from KST: please remove this line if doing any edits by hand!

extern crate kaitai_struct;
extern crate rust;

use kaitai_struct::KaitaiStruct;
use rust::ProcessRepeatBytes;

#[test]
fn test_process_repeat_bytes() {
    if let Ok(r) = ProcessRepeatBytes::from_file("src/process_xor_4.bin") {

        assert_eq!(r.bufs[0], vec!([0x72, 0x25, 0x3d, 0x8a, 0x14]));
        assert_eq!(r.bufs[1], vec!([0x4a, 0x52, 0xaa, 0x10, 0x44]));
    }
}
