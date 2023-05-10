import time

import uiautomator2 as ut2
d=ut2.connect('emulator-5554')  #通过ut连接到安卓及其，而且获取到设备
print(d.info)

#黑屏
# d.screen_off()
#
# #点亮
# d.screen_on()
#
# #返回桌面
# d.press('home')

#打开app
# d.app_start('com.tencent.mtt.x86')

# d.app_stop('com.android.flysilkworm')
# d.app_clear('com.android.flysilkworm')
d.app_start('com.ophone.reader.ui')
time.sleep(14)
d.xpath('//*[@content-desc="借书"]/android.view.View[1]').click()
time.sleep(3)

# d.xpath('//*[@resource-id="com.ophone.reader.ui:id/sso_login_username_layout"]').set_text('1056')
#
# time.sleep(1)
# d.xpath('//*[@resource-id="com.ophone.reader.ui:id/sso_login_password_edt"]').set_text("6446")
# time.sleep(2)
# d.click(0.691, 0.498)
# d.send_keys("1", clear=True)
# d.swipe(0.481, 0.364,0.481,0.525)
# d.click()
# d.swipe_points([(x0, y0), (x1, y1), (x2, y2)], 0.2))
d(scrollable=True).scroll.to(text="闻人凡梦zods")
d.screenshot("./home.jpg")