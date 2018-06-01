import unittest


class TestSub(unittest.TestCase):
    def setUp(self):
        pass

    def test_sub(self):
        self.assertEqual(16 - 5, 11)

    def test_sub2(self):
        self.assertEqual(15 - 7, 8)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()