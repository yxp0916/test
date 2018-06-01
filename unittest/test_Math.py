from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_addis(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)

    def test_addno(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(),12)

    def test_addxiao(self):
        j=Math(5,10)
        self.assertTrue(j.add() < 130)

    def testin(self):
        self.assertIn("51zxw", "Hello,51zxw")

    def testis(self):
        self.assertIs("51zxw3", "51zxw3")

    def testin2(self):
        self.assertIn("51zwwwxw","Hello,51zxw")

    def tearDown(self):
        print("test end!")

# if __name__=='__main__':
#     unittest.main()
suite=unittest.TestSuite()
suite.addTest(TestMath('test_addis'))
suite.addTest(TestMath('test_addno'))
suite.addTest(TestMath('test_addxiao'))
suite.addTest(TestMath('testin'))
suite.addTest(TestMath('testis'))
suite.addTest(TestMath('testin2'))

runner=unittest.TextTestRunner()
runner.run(suite)