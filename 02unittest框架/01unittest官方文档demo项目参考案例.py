# unittest官方文档demo项目参考案例，
'''
一个用例class继承unittest.TestCase类（就是我们想要继承unittest进行自动化测试，就需要一个写一个用例类继承unittest模块里面的这个TestCase类），
用例类里面的方法即是一个个具体的测试用例TestCase

书写规范：
类方法名称必须以 test 开头，否则是不被unittest识别成用例
类的名称可以不以test开头


'''
import unittest

# 单元测试方法测试用例
       #类名称随意
class TestStringMethods(unittest.TestCase):

         #test开头命名，测试用例
    def test_upper(self):

      self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):

      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())


    def test_split(self):


      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
# check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
       s.split(2)
if __name__ == '__main__':
    unittest.main()
