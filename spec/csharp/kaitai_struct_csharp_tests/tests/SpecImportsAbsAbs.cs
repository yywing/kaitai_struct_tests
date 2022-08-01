using NUnit.Framework;

namespace Kaitai
{
    [TestFixture]
    public class SpecImportsAbsAbs : CommonSpec
    {
        [Test]
        public void TestImportsAbsAbs()
        {
            var r = ImportsAbsAbs.FromFile(SourceFile("fixed_struct.bin"));

            Assert.AreEqual(r.One, 80);
            Assert.AreEqual(r.Two.One, 65);
            Assert.AreEqual(r.Two.Two.One, 67);
        }
    }
}
