# Autogenerated from KST: please remove this line if doing any edits by hand!

RSpec.describe 'EnumFancy' do
  it 'parses test properly' do
    require 'enum_fancy'
    r = EnumFancy.from_file('src/enum_0.bin')

    expect(r.pet_1).to eq :animal_cat
    expect(r.pet_2).to eq :animal_chicken
  end
end
