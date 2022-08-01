# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'BitsByteAligned' do
  it 'parses test properly' do
    require 'bits_byte_aligned'
    r = BitsByteAligned.from_file('src/fixed_struct.bin')

    expect(r.one).to eq 20
    expect(r.byte_1).to eq 65
    expect(r.two).to eq 2
    expect(r.three).to eq false
    expect(r.byte_2).to eq 75
    expect(r.four).to eq 2892
    expect(r.byte_3).to eq [255].pack('C*')
    expect(r.full_byte).to eq 255
    expect(r.byte_4).to eq 80
  end
end
