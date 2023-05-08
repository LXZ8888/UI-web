import unittest
'''仅仅作为辅助用例模板，unittests案例A的导入模板'''


class B01(unittest.TestCase):
    def testcase010(self):
        print('模块B测试用例1')

     #冒烟测试用例
    def testcase020(self):
        print('模块B测试用例2')

    def testcase03(self):

        print('模块B测试用例3')

    # 冒烟测试用例
    def testcase04(self):

        self.assertEqual(1,0)      # unittets自带的断言方法   #判断1和0是否相等   # 报错 self.assertEqual(1,0)  #判断1和0是否相等   AssertionError: 1 != 0'''
        print('模块B测试用例4')

    def testcase05(self):
        print('模块B测试用例5')

        #命名不合规范，不被执行，没有识别到。语法 E(语法错误)
    def yestcase05(self):
        print('模块B测试用例555')



class YinuoTestcase02(unittest.TestCase):
    def testcase010(self):
        print('模块B测试用例06')

    def testcase020(self):
        print('模块2测试用例07')



#所有用例执行：unittest.main()方法会运行当前py文件中，所有继承了unittest.TestCase的类里面的测试用例（以test开头的函数）
# unittest.main(verbosity=2)       #所有用例都执行的方法


#指定用例执行，一个类/多个类部分用例运行
if __name__ == '__main__':
    testcases = unittest.TestSuite()   #步骤一：实例化。创建一个测试套件  。（相当于一个容器里面装用例然后运行）
    testcases.addTests([YinuoTestcase01('testcase010'), YinuoTestcase02('testcase020')])   #步骤二：列表。往测试套件添加测试用例TestYiNuo
    runner = unittest.TextTestRunner()   #步骤三：实例化对象过程。一个基础的测试执行器，实现了将结果输出为流的功能。
    runner.run(testcases)                  #调用


'''运行结果
..E..        E(语法错误)
FAILED (errors=1)
模块2测试用例1
模块2测试用例1
模块2测试用例1
模块2测试用例1
测试用例3错误，所以不执行。没有影响其他测试用例.unittest
'''