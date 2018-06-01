import unittest

import testadd2
import testsub

suite = unittest.TestSuite()
suite.addTest(testadd2.TestAdd('test_add'))
suite.addTest(testadd2.TestAdd('test_add2'))
suite.addTest(testadd2.TestAdd('test_add3'))

suite.addTest(testsub.TestSub('test_sub'))
suite.addTest(testsub.TestSub('test_sub2'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
