from test_Count import Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print("test start:")

    def test_add(self):
        j=Count(5,6)
        self.assertEqual(j.add(),121)

    def test_add2(self):
        j=Count(12,11)
        self.assertEqual(j.add(),23)

    def tearDown(self):
        print("test end!")

if __name__=='__main__':
    suite=unittest.TestSuite
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add2"))
    runner=unittest.TextTestRunner
    runner.run(suite)