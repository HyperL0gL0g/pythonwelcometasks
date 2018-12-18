import subprocess
import os
import webbrowser

print("----------------------WELCOME TO START UP MENU-------------------")

print("press 1 for opening GOOGLE CHROME")
print("press 2 for playing PUBG MOBILE")
print("press 3 for opening D:STORAGE")
print("press 4 for KIIT sap portal")
print("press 5 for OPENING GAMES FOLDER")
print("press 6 for YOUTUBE.COM")
print("press 7 to quit this window")

print("--------------------------------END------------------------------")
choice = input("what is your choice? ")
if choice=="1":subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
elif choice=="3":os.startfile('D:\STORAGE') 
elif choice=="2":os.startfile('D:\Program Files\TxGameAssistant\AppMarket\AppMarket')
elif choice=="4":webbrowser.open_new("http://kiitportal.kiituniversity.net/irj/portal")
elif choice=="6":webbrowser.open_new("https://www.youtube.com")
elif choice=="5":os.startfile('D:\GAMES') 
elif choice=="7":quit()











