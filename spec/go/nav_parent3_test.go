// Autogenerated from KST: please remove this line if doing any edits by hand!

package spec

import (
	"runtime/debug"
	"os"
	"testing"
	"github.com/kaitai-io/kaitai_struct_go_runtime/kaitai"
	. "test_formats"
	"github.com/stretchr/testify/assert"
)

func TestNavParent3(t *testing.T) {
	defer func() {
		if r := recover(); r != nil {
			debug.PrintStack()
			t.Fatal("unexpected panic:", r)
		}
	}()
	f, err := os.Open("../../src/nav_parent2.bin")
	if err != nil {
		t.Fatal(err)
	}
	s := kaitai.NewStream(f)
	var r NavParent3
	err = r.Read(s, &r, &r)
	if err != nil {
		t.Fatal(err)
	}

	assert.EqualValues(t, 8, r.OfsTags)
	assert.EqualValues(t, 2, r.NumTags)
	tmp1, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "RAHC", tmp1[0].Name)
	tmp2, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, 32, tmp2[0].Ofs)
	tmp3, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, 3, tmp3[0].NumItems)
	tmp4, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	tmp5, err := tmp4[0].TagContent()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "foo", tmp5.Content)
	tmp6, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "RAHC", tmp6[1].Name)
	tmp7, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, 35, tmp7[1].Ofs)
	tmp8, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, 6, tmp8[1].NumItems)
	tmp9, err := r.Tags()
	if err != nil {
		t.Fatal(err)
	}
	tmp10, err := tmp9[1].TagContent()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "barbaz", tmp10.Content)
}
