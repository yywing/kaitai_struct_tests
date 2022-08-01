# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'ProcessCoerceBytes' do
  it 'parses test properly' do
    require 'process_coerce_bytes'
    r = ProcessCoerceBytes.from_file('src/process_coerce_bytes.bin')

    expect(r.records[0].flag).to eq 0
    expect(r.records[0].buf).to eq [65, 65, 65, 65].pack('C*')
    expect(r.records[1].flag).to eq 1
    expect(r.records[1].buf).to eq [66, 66, 66, 66].pack('C*')
  end
end
