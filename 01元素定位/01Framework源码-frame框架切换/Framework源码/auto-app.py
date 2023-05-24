import uiautomator2 as ut2

d = ut2.connect('emulator-5554')
print(d.device_info)
