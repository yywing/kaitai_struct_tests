# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'NavParentSwitchCast' do
  it 'parses test properly' do
    require 'nav_parent_switch_cast'
    r = NavParentSwitchCast.from_file('src/switch_integers.bin')

    expect(r.main.buf_type).to eq 1
    expect(r.main.flag).to eq 7
    expect(r.main.buf.branch.flag).to eq 7
  end
end
