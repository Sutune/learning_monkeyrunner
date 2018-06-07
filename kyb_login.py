# -*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi


print("connect devices...")
device=mr.waitForConnection(5,'127.0.0.1:62001')
device.installPackage(r'C:\Users\Shuqing\Desktop\Appium\kaoyan3.1.8.apk')

print("set app info")
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent = package + '/' + activity

print("launchApp...")
device.startActivity(component=runComponent)
mr.sleep(5)

print("touch cancel button")
device.touch(190,777,'DOWN_AND_UP')  
mr.sleep(4)

print("touch skip button")
device.touch(649,53,'DOWN_AND_UP')

print("input username and password ")
device.touch(151,285,'DOWN_AND_UP')
mr.sleep(3)
device.type('zxw1234')
mr.sleep(2)
device.touch(156,354,'DOWN_AND_UP')
mr.sleep(3)
device.type('zxw123456')

print("touch login button")
device.touch(275,475,'DOWN_AND_UP')
mr.sleep(4)

print("takeSnapshot")
screenshot=device.takeSnapshot()  
screenshot.writeToFile(r'E:\monkeyrunner_script\test.png','png')  

print("agree licence")
device.touch(539,844,'DOWN_AND_UP')
mr.sleep(3)
'''
print("touch community button")
device.touch(365,1233,'DOWN_AND_UP')
mr.sleep(3)
device.touch(365,1233,'DOWN_AND_UP')
mr.sleep(3)

print("drag the screen")
start = (334,1145)
end = (331,291)
duration = 1.5
steps = 12
device.drag(start,end,duration,steps)
mr.sleep(3)

device.touch(275,475,'DOWN_AND_UP')
mr.sleep(5)

device.touch(36,69,'DOWN_AND_UP')

'''


