# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'BitsSignedResB32Be' do
  it 'parses test properly' do
    require 'bits_signed_res_b32_be'
    r = BitsSignedResB32Be.from_file('src/bits_shift_by_b32_le.bin')

    expect(r.a).to eq 4294967295
  end
end
