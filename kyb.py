# -*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md


print("connect devices...")
device=mr.waitForConnection()

print("install app...")
device.installPackage(r'C:\Users\Shuqing\Desktop\kaoyan3.1.0.apk')

package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent = package + '/' + activity

print("launchApp...")
device.startActivity(component=runComponent)
mr.sleep(3)



