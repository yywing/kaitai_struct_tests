# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'ParamsPassArrayStr' do
  it 'parses test properly' do
    require 'params_pass_array_str'
    r = ParamsPassArrayStr.from_file('src/term_strz.bin')

    expect(r.pass_str_array.strs.length).to eq 3
    expect(r.pass_str_array.strs[0]).to eq "fo"
    expect(r.pass_str_array.strs[1]).to eq "o|"
    expect(r.pass_str_array.strs[2]).to eq "ba"
    expect(r.pass_str_array_calc.strs.length).to eq 2
    expect(r.pass_str_array_calc.strs[0]).to eq "aB"
    expect(r.pass_str_array_calc.strs[1]).to eq "Cd"
  end
end
