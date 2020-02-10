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

func TestStrCombine(t *testing.T) {
	defer func() {
		if r := recover(); r != nil {
			debug.PrintStack()
			t.Fatal("unexpected panic:", r)
		}
	}()
	f, err := os.Open("../../src/term_strz.bin")
	if err != nil {
		t.Fatal(err)
	}
	s := kaitai.NewStream(f)
	var r StrCombine
	err = r.Read(s, &r, &r)
	if err != nil {
		t.Fatal(err)
	}

	assert.EqualValues(t, "foo", r.StrTerm)
	assert.EqualValues(t, "bar|", r.StrLimit)
	assert.EqualValues(t, "baz@", r.StrEos)
	tmp1, err := r.StrCalc()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "bar", tmp1)
	tmp2, err := r.StrCalcBytes()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "baz", tmp2)
	tmp3, err := r.TermOrLimit()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "foo", tmp3)
	tmp4, err := r.TermOrEos()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "baz@", tmp4)
	tmp5, err := r.TermOrCalc()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "foo", tmp5)
	tmp6, err := r.TermOrCalcBytes()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "baz", tmp6)
	tmp7, err := r.LimitOrEos()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "bar|", tmp7)
	tmp8, err := r.LimitOrCalc()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "bar", tmp8)
	tmp9, err := r.LimitOrCalcBytes()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "bar|", tmp9)
	tmp10, err := r.EosOrCalc()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "bar", tmp10)
	tmp11, err := r.EosOrCalcBytes()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "baz@", tmp11)
	tmp12, err := r.CalcOrCalcBytes()
	if err != nil {
		t.Fatal(err)
	}
	assert.EqualValues(t, "baz", tmp12)
}
