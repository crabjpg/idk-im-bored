import time
import os
import random as r
pid = r.randint(1000, 99999)
cnum = 0
exe = "csgo.exe"
stat1 = 0
stat2 = 0
stat3 = 0
stat4 = 0
stat5 = 0


aaa = input("Welcome to ReLoad for CS:GO. Press 'enter' to attach.")
while cnum < 100:
    print("Attaching. " + str(cnum) + "%")
    cnum = cnum + 1
    time.sleep(0.1)
    os.system('cls')
if cnum == 100:
    print("Injection complete! Loading Cheat...")
    time.sleep(10)
    print("Loaded!")

while True:
    print("{1} [" + str(stat1) + "] Aim Assist")
    print("{2} [" + str(stat2) + "] Anti Aim")
    print("{3} [" + str(stat3) + "] Sound ESP")
    print("{4} [" + str(stat4) + "] Quick Reload")
    print("{5} [" + str(stat5) + "] Quick Plant Bomb")
    print("{6} [/] Exit and Unattach")
    funcchoice = input("Please choose a number.")
    if funcchoice == "1":
        if stat1 == 0:
            print("Enabling Aim Assist")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Enabled! Returning to menu...")
            stat1 = 1
            time.sleep(5)
            continue
        if stat1 == 1:
            print("Disabling Aim Assist")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Disabled! Returning to menu...")
            stat1 = 0
            time.sleep(5)
            continue
    if funcchoice == "2":
        if stat2 == 0:
            print("Enabling Anti Aim")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Enabled! Returning to menu...")
            stat2 = 1
            time.sleep(5)
            continue
        if stat2 == 1:
            print("Disabling Anti Aim")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Disabled! Returning to menu...")
            stat2 = 0
            time.sleep(5)
            continue
    if funcchoice == "3":
        if stat3 == 0:
            print("Enabling Sound ESP")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Enabled! Returning to menu...")
            stat3 = 1
            time.sleep(5)
            continue
        if stat3 == 1:
            print("Disabling Sound ESP")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Disabled! Returning to menu...")
            stat3 = 0
            time.sleep(5)
            continue
    if funcchoice == "4":
        if stat4 == 0:
            print("Enabling Quick Reload")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Enabled! Returning to menu...")
            stat4 = 1
            time.sleep(5)
            continue
        if stat4 == 1:
            print("Disabling Quick Reload")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Disabled! Returning to menu...")
            stat4 = 0
            time.sleep(5)
            continue
    if funcchoice == "5":
        if stat5 == 0:
            print("Enabling Quick Plant Bomb")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Enabled! Returning to menu...")
            stat5 = 1
            time.sleep(5)
            continue
        if stat5 == 1:
            print("Disabling Quick Plant Bomb")
            time.sleep(5)
            for i in range(16):
                theprinter = r.randint(10000000, 99999999)
                print(theprinter)
                os.system('cls')
            print("Disabled! Returning to menu...")
            stat5 = 0
            time.sleep(5)
            continue
    if funcchoice == "6":
        exit("Unhooked and Disabled")