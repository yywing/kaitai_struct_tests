// Autogenerated from KST: please remove this line if doing any edits by hand!

using NUnit.Framework;

namespace Kaitai
{
    [TestFixture]
    public class SpecValidFailRangeStr : CommonSpec
    {
        [Test]
        public void TestValidFailRangeStr()
        {
            Assert.Throws<ValidationGreaterThanError>(
                delegate
                {
                    ValidFailRangeStr.FromFile(SourceFile("fixed_struct.bin"));
                }
            );
        }
    }
}
