# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'SwitchRepeatExpr' do
  it 'parses test properly' do
    require 'switch_repeat_expr'
    r = SwitchRepeatExpr.from_file('src/switch_tlv.bin')

    expect(r.code).to eq 17
    expect(r.size).to eq 9
    expect(r.body[0].first).to eq [83, 116, 117, 102, 102, 0, 77, 101, 0].pack('C*')
  end
end
