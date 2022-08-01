# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'ProcessRotate' do
  it 'parses test properly' do
    require 'process_rotate'
    r = ProcessRotate.from_file('src/process_rotate.bin')

    expect(r.buf1).to eq [72, 101, 108, 108, 111].pack('C*')
    expect(r.buf2).to eq [87, 111, 114, 108, 100].pack('C*')
    expect(r.buf3).to eq [84, 104, 101, 114, 101].pack('C*')
  end
end
