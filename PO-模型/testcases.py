'''用例类：只有业务关键字+断言'''
import time
import unittest
from selenium import webdriver
from LoginPage import LoginPage
from HomePage import HomePage
from InitBrowser import Browser
import warnings
class ScTestCases(unittest.TestCase,LoginPage,HomePage):

    @classmethod
    def setUpClass(self) -> None:
        warnings.simplefilter("ignore", ResourceWarning)
        '''前置：打开被测项目'''
        self.driver = webdriver.Chrome() #浏览器对象
        self.driver.get('http://42.192.6.197/?s=user/loginInfo.html') #打开电商商城系统
        d=Browser(self.driver)
    def tearDown(self) -> None:
        '''后置：用例运行完成等待几秒'''
        time.sleep(2)

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()
    def test_01_login(self):
        '''普通脚本'''
        driver=self.driver
        '''第一次优化：集成PO'''
        '''第二次优化：元素的定位方式放到PO统一管理'''
        '''第三次优化：业务步骤'''
        #self.type_unsername('qingfeng')
        #self.type_password('123456')
        #self.type_login_button()

        '''第四次优化：封装业务关键字（常用绑定在一起的）
        2-3步骤
        '''

        '''第五次优化：每次操作一个元素，自动加上显式等待时间，
        封装等待时间方法
        日志打印方法，
        错误截图方法
        封装到浏览器基础类
        '''
        self.login('admin1','shopxo')
        self.search('包包')



if __name__ == '__main__':
    unittest.main()