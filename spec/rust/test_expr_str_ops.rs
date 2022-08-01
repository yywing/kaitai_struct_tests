// Autogenerated from KST: please remove this line if doing any edits by hand!

extern crate kaitai_struct;
extern crate rust;

use kaitai_struct::KaitaiStruct;
use rust::ExprStrOps;

#[test]
fn test_expr_str_ops() {
    if let Ok(r) = ExprStrOps::from_file("src/term_strz.bin") {

        assert_eq!(r.one, "foo|b");
        assert_eq!(r.one_len, 5);
        assert_eq!(r.one_rev, "b|oof");
        assert_eq!(r.one_substr_0_to_3, "foo");
        assert_eq!(r.one_substr_2_to_5, "o|b");
        assert_eq!(r.one_substr_3_to_3, "");
        assert_eq!(r.two, "0123456789");
        assert_eq!(r.two_len, 10);
        assert_eq!(r.two_rev, "9876543210");
        assert_eq!(r.two_substr_0_to_7, "0123456");
        assert_eq!(r.two_substr_4_to_10, "456789");
        assert_eq!(r.two_substr_0_to_10, "0123456789");
        assert_eq!(r.to_i_attr, 9173);
        assert_eq!(r.to_i_r10, -72);
        assert_eq!(r.to_i_r2, 86);
        assert_eq!(r.to_i_r8, 465);
        assert_eq!(r.to_i_r16, 18383);
    }
}
