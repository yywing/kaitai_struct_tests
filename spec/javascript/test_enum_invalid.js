// Autogenerated from KST: please remove this line if doing any edits by hand!

var assert = require('assert');
var testHelper = require('testHelper');

testHelper('EnumInvalid', 'src/term_strz.bin', function(r, EnumInvalid) {

  assert.strictEqual(r.pet1, EnumInvalid.Animal.DOG);
  assert.strictEqual(r.pet2, 111);
});
