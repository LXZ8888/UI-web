import time
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class TestStringMethods(unittest.TestCase):
    #前置操作执行一次-因为只想要打开一次浏览器
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://42.192.6.197/')

    # 前置操作-setup
    # def setUp(self) -> None:
    #     '''打开被测项目'''
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://42.192.6.197/')
    @unittest.skip('不想运行这用例')
    # @unittest.skipIf(3>2,'因为3>2')
    # @unittest.skipUnless(3<2,'假才执行')
    def login(self):
        '用例1: 登录'
        # self.driver = webdriver.Chrome()
        self.driver.get('http://42.192.6.197/?s=user/logininfo.html')
        self.driver.find_element_by_xpath('//*[@placeholder="请输入用户名/手机/邮箱"]').send_keys('admin1')
        self.driver.find_element_by_xpath('//*[@placeholder="请输入登录密码"]').send_keys('shopxo')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()

    def test_search(self):
        '''用例2: 搜索手机'''

        self.driver.find_element_by_id('search-input').send_keys('手机')
        self.driver.find_element_by_id('ai-topsearch').click()


    def test_search_by_price(self):

        self.driver.find_element_by_xpath('//*[@id="search-map"]/div/div/ul/li[4]/div[2]/ul/li[6]/a').click()
            #断言,搜索价格1500-2000价格的手机的一条数据,查找元素，返回列表，然后len
        time.sleep(2)
        res=len(self.driver.find_elements_by_xpath('/html/body/div[5]/div/ul/li/div'))
        self.assertEqual(res,1)

    


if __name__ == '__main__':
    unittest.main(verbosity=2)
