import unittest
from unittets0B import B01


#总结:看思维导图。案例包含：unittest基础语法规则、unittest用例执行（全部用例，部分用例，A-B，指定类用例 执行）
# 类方法名称必须以 test 开头，否则是不被unittest识别成用例
# 类的名称可以不以test开头
'''
高效的执行用例，批量执行用例，执行部分冒烟用例，执行多个文件的用例
某一个用例失败不影响其他用例正常运行
丰富的断言方法

控制台：unittest.main(verbosity=2)。verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告
'''
class YinuoTestcase01(unittest.TestCase):
    def testcase010(self):
        print('模块2测试用例1')

     #冒烟测试用例
    def testcase020(self):
        print('模块2测试用例2')

    def testcase03(self):
        a = 1 / 0
        print('模块2测试用例3')

    # 冒烟测试用例
    def testcase04(self):

        self.assertEqual(1,0)      # unittets自带的断言方法   #判断1和0是否相等   # 报错 self.assertEqual(1,0)  #判断1和0是否相等   AssertionError: 1 != 0'''
        print('模块2测试用例4')

    def testcase05(self):
        print('模块2测试用例5')

        #命名不合规范，不被执行，没有识别到。语法 E(语法错误)
    def yestcase05(self):
        print('模块2测试用例555')



class YinuoTestcase02(unittest.TestCase):
    def testcase010(self):
        print('模块2测试用例06')

    def testcase020(self):
        print('模块2测试用例07')



#所有用例执行：unittest.main()方法会运行当前py文件中，所有继承了unittest.TestCase的类里面的测试用例（以test开头的函数）
# unittest.main(verbosity=2)       #所有用例都执行的方法


#指定用例执行，一个类/多个类(多个py文件)部分用例运行
# if __name__ == '__main__':
#     testcases = unittest.TestSuite()   #步骤一：实例化。创建一个测试套件  。（相当于一个容器里面装用例然后运行）
    #     testcases.addTests([YinuoTestcase01('testcase010'),B01('testcase020')])   #步骤二：列表。往测试套件添加测试用例TestYiNuo
#     runner = unittest.TextTestRunner()   #步骤三：实例化对象过程。一个基础的测试执行器，实现了将结果输出为流的功能。
#     runner.run(testcases)                  #调用


#指定类里面的全部用例执行
if __name__ == '__main__':
    testcases = unittest.TestSuite()   #步骤一：实例化。创建一个测试套件  。（相当于一个容器里面装用例然后运行）
    #添加一个类，指定类里面的用例全部执行
    testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(YinuoTestcase02))   #步骤二：列表。往测试套件添加测试用例TestYiNuo
    #再添加一个类，在重复写一遍，因为loadTestsFromTestCase（参数）参数只能填一个，不能是列表
    testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(YinuoTestcase01))
    runner = unittest.TextTestRunner()   #步骤三：实例化对象过程。一个基础的测试执行器，实现了将结果输出为流的功能。
    runner.run(testcases)                  #调用
    #运行结果Ran 2 tests in 0.000s OK 模块2测试用例06  模块2测试用例07






'''运行结果
..E..        E(语法错误)
FAILED (errors=1)
模块2测试用例1
模块2测试用例1
模块2测试用例1
模块2测试用例1
测试用例3错误，所以不执行。没有影响其他测试用例.unittest
'''