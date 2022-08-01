// Autogenerated from KST: please remove this line if doing any edits by hand!

package spec

import (
	"runtime/debug"
	"os"
	"testing"
	"github.com/kaitai-io/kaitai_struct_go_runtime/kaitai"
	. "test_formats"
)

func TestValidFailEqStr(t *testing.T) {
	defer func() {
		if r := recover(); r != nil {
			debug.PrintStack()
			t.Fatal("unexpected panic:", r)
		}
	}()
	f, err := os.Open("../../src/fixed_struct.bin")
	if err != nil {
		t.Fatal(err)
	}
	s := kaitai.NewStream(f)
	var r ValidFailEqStr
	err = r.Read(s, &r, &r)
	switch v := err.(type) {
	case kaitai.ValidationNotEqualError:
		break
	default:
		t.Fatalf("expected kaitai.ValidationNotEqualError, got %T", v)
	}
}
