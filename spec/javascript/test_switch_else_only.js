// Autogenerated from KST: please remove this line if doing any edits by hand!

var assert = require('assert');
var testHelper = require('testHelper');
var hexString = require('hexString');

testHelper('SwitchElseOnly', 'src/switch_opcodes.bin', function(r, SwitchElseOnly) {

  assert.strictEqual(r.opcode, 83);
  assert.strictEqual(r.primByte, 102);
  assert.strictEqual(hexString(r.ut.value), hexString([114, 0, 73, 66]));
});
