import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
driver=webdriver.Chrome()
driver.get("https://www.kuaidi100.com/")

#is_displayed() 用于判断某个元素是否存在页面上，返回的是一个布尔值

# t=driver.find_element_by_id('uDeskTarget').is_displayed()
# print(t)
driver.find_element_by_id('uDeskTarget').click()

#切换frame
driver.switch_to.frame('udesk_iframe')

#显示等待 visibility_of_element_located(参数类型为元祖)
#WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="footer"]/div[2]/div[2]/textarea')))
# driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div[2]/textarea').send_keys('小姐姐你好')

#匿名函数实现显示等待  调用until方法的时候，源代码会自动传一个参数driver

# a=lambda x,y:x+y
# print(a(2,6))

'''
no such element: Unable to locate element 元素还在加载
element not interactable 
'''
WebDriverWait(driver,16). until(lambda x : x.find_element(By.XPATH,'//*[@id="footer"]/div[2]/div[2]/textarea').is_displayed()) #driver.find_element()
driver.find_element_by_xpath('//*[@id="footer"]/div[2]/div[2]/textarea').send_keys('11111')




#业务操作。点击另一个按钮，每个业务操作之前加上显示等待，保证脚本稳定，需要把显示等待封装到一个公共方法：pom

