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
        # driver.find_element_by_name('accounts').send_keys('yinuo')
        # driver.find_element_by_name('pwd').send_keys('123456')
        # driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button").click()

        '''第一次优化：集成PO'''
        '''第二次优化：元素的定位方式放到PO统一管理'''
        '''第三次优化：业务步骤'''
        #self.type_unsername('qingfeng')
        #self.type_password('123456')
        #self.type_login_button()

        '''第四次优化：封装业务关键字（常用绑定在一起的）
        2-3步骤
        '''
        # self.login('qingfeng','123456')
        # self.search('包包')

        '''第五次优化：每次操作一个元素，自动加上显式等待时间，
        封装等待时间方法
        日志打印方法，
        错误截图方法
        封装到浏览器基础类
        '''
        self.login('admin1','shopxo')
        self.search('包包')


        # def test_02_search(self):
    #     '''用例1：商品搜索'''
    #     self.driver.find_element_by_id('search-input').send_keys('手机')
    #     self.driver.find_element_by_id('ai-topsearch').click()
    #
    # #@unittest.skipUnless(3<2,'因为3大于，理由')
    # def test_03_search_by_price(self):
    #     '''用例2：根据价格进行搜索'''
    #     '''筛选价格'''
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath("//*[text()='2000-3000']").click()
    #     '''断言：搜索3条价格为2-3k的手机'''
    #     time.sleep(2)
    #     res=len(self.driver.find_elements_by_xpath("//*[@class='am-animation-scale-up']"))
    #     self.assertEqual(res,2)


if __name__ == '__main__':
    unittest.main()