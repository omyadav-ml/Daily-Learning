import os

print("Current Directory:",os.getcwd())
# It will shows current working directory

print('Files in folder',os.listdir())
# It will list all the file in  current folder




import random 

print("Random Number:",random.randint(1,100))

programming_lang=["Cpp","C","Python",'Java',"Javascript"]
print("Random lang:",random.choice(programming_lang))




import datetime

now = datetime.datetime.now()
print("Current Date and Time:", now)

today = datetime.date.today()
print("Today's Date:", today)

print("Year:", today.year, "Month:", today.month, "Day:", today.day)




import calendar
print(calendar.month(2025, 11))




import pyfiglet
font = pyfiglet.figlet_format('Om Yadav')
print(font)



import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())