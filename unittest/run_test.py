import unittest
import test_baidu,test_youdao

suite = unittest.TestSuite()
suite.addTest(test_baidu.BaiduTest('test_baidu'))
suite.addTest(test_youdao.YoudaoTest('test_youdao'))

# if __name__=='__main__':
runner = unittest.TextTestRunner()
runner.run(suite)