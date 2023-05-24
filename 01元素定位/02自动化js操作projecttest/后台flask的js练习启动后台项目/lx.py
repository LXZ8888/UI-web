from selenium import webdriver

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.execute_script('window.open("https://taobao.com")')
