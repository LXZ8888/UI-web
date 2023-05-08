import unittest
# from unittets0B import B01
'''
每个用例的前置和后置：就是所有用例运行执行，首先都会执行一遍前置操作。前置执行：相当于夹心饼干一样，前置执行-在测试用例01-每个用例的后置，前置执行-测试用例02-每个用例的后置
'''

class YinuoTestcase01(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('所有用例的前置操作-头---最先执行，执行一次')

    @classmethod
    def tearDownClass(self) -> None:
        print('所有用例的后置操作-尾---最后执行，执行一次')

    def setUp(self) -> None:
        print('每个用例的前置')
    def tearDown(self) -> None:
        print('每个用例的后置')

     #冒烟测试用例
    def testcase020(self):
        print('模块2测试用例2')

    def testcase03(self):

        print('模块2测试用例3')

    # 冒烟测试用例
    def testcase04(self):

        self.assertEqual(1,0)
        print('模块2测试用例4')

    def testcase05(self):
        print('模块2测试用例5')

        #命名不合规范，不被执行，没有识别到。语法 E(语法错误)
    def yestcase05(self):
        print('模块2测试用例555')



# class YinuoTestcase02(unittest.TestCase):
#     def testcase010(self):
#         print('模块2测试用例06')
#
#     def testcase020(self):
#         print('模块2测试用例07')



#所有用例执行：unittest.main()方法会运行当前py文件中，所有继承了unittest.TestCase的类里面的测试用例（以test开头的函数）
# unittest.main(verbosity=2)       #所有用例都执行的方法


#指定用例执行，一个类/多个类(多个py文件)部分用例运行
if __name__ == '__main__':
    unittest.main(verbosity=2)

