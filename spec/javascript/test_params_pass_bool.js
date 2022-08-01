// Autogenerated from KST: please remove this line if doing any edits by hand!

var assert = require('assert');
var testHelper = require('testHelper');

testHelper('ParamsPassBool', 'src/term_strz.bin', function(r, ParamsPassBool) {

  assert.strictEqual(r.sFalse, false);
  assert.strictEqual(r.sTrue, true);
  assert.strictEqual(r.seqB1.arg, true);
  assert.strictEqual(r.seqB1.foo.length, 1);
  assert.strictEqual(r.seqBool.arg, false);
  assert.strictEqual(r.seqBool.foo.length, 2);
  assert.strictEqual(r.literalB1.arg, false);
  assert.strictEqual(r.literalB1.foo.length, 2);
  assert.strictEqual(r.literalBool.arg, true);
  assert.strictEqual(r.literalBool.foo.length, 1);
  assert.strictEqual(r.instB1.arg, true);
  assert.strictEqual(r.instB1.foo.length, 1);
  assert.strictEqual(r.instBool.arg, false);
  assert.strictEqual(r.instBool.foo.length, 2);
});
