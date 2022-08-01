# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'CombineStr' do
  it 'parses test properly' do
    require 'combine_str'
    r = CombineStr.from_file('src/term_strz.bin')

    expect(r.str_term).to eq "foo"
    expect(r.str_limit).to eq "bar|"
    expect(r.str_eos).to eq "baz@"
    expect(r.str_calc).to eq "bar"
    expect(r.str_calc_bytes).to eq "baz"
    expect(r.term_or_limit).to eq "foo"
    expect(r.term_or_eos).to eq "baz@"
    expect(r.term_or_calc).to eq "foo"
    expect(r.term_or_calc_bytes).to eq "baz"
    expect(r.limit_or_eos).to eq "bar|"
    expect(r.limit_or_calc).to eq "bar"
    expect(r.limit_or_calc_bytes).to eq "bar|"
    expect(r.eos_or_calc).to eq "bar"
    expect(r.eos_or_calc_bytes).to eq "baz@"
    expect(r.calc_or_calc_bytes).to eq "baz"
  end
end
