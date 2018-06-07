# -*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi


print("connect devices...")
device=mr.waitForConnection(5,'127.0.0.1:62001')
#device.installPackage(r'C:\Users\Shuqing\Desktop\Appium\kaoyan3.1.8.apk')

print("set app info")
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent = package + '/' + activity

print("launchApp...")
device.startActivity(component=runComponent)
mr.sleep(4)

print("touch skip button")
device.touch(649,53,'DOWN_AND_UP')
mr.sleep(4)

print("touch community button")
device.touch(365,1233,'DOWN_AND_UP')
mr.sleep(3)


start = (334,1145)
end = (331,291)
duration = 2
steps = 12
print("drag the screen...")
device.drag(start,end,duration,steps)
mr.sleep(3)

print("open article")
device.touch(275,475,'DOWN_AND_UP')
mr.sleep(5)

