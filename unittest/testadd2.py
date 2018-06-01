import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(2 + 3, 5, "testError")

    def test_add2(self):
        self.assertEqual(0 + 8, 8, "testError")

    def test_add3(self):
        self.assertIn("51zddxw", "Hello,51zxw")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()