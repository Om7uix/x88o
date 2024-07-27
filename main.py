try:
  import keyboard
  import threading
  import time
  import os
  import subprocess
  from colorama import Fore, Style,init
  from pathlib import Path
  from os import path



except ModuleNotFoundError:
        subprocess.call("pip3 install keyboard", shell=True)
        subprocess.call("pip3 install colorama", shell=True)
        

banner = r'''
 _____ ______   ___  ___  ___  _____  _____  _____  _     
/  ___|| ___ \ / _ \ |  \/  | |_   _||  _  ||  _  || |    
\ `--. | |_/ // /_\ \| .  . |   | |  | | | || | | || |    
 `--. \|  __/ |  _  || |\/| |   | |  | | | || | | || |    
/\__/ /| |    | | | || |  | |   | |  \ \_/ /\ \_/ /| |____
\____/ \_|    \_| |_/\_|  |_/   \_/   \___/  \___/ \_____/
                                                          
                            
                         Developers : Omar Sameh .                               

'''
print(Style.BRIGHT+Fore.RED+banner+Fore.RESET)





      
class spam :
    def checkfile(self) :
        if path.exists('spam.txt'):
           ask = input(str("File already Present\nDo you want to use me ? (y or n) : "))
           if "y" in ask :
                self.write()      
                self.spams()
           else :
             self.spams()
        else :
         self.write()

    def write(self):
        try:
            f = open('spam.txt', 'w')
        except IOError:
            print("Error opening the file.")
            return

        while True:
            try:
                s = int(input("How Many Lines U Want To Spam : "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        for i in range(s):
            n = input("Enter the characters you want to write: ")
            f.write(n + '\n')


        f.write(n)
        f.write("\n")
    
       

    def spams(self):
        print("Now You Can Use Me For Spam :) ")
        time.sleep(5)
        while True:
        
           file=open("spam.txt", 'r')
           x=file.read()
           keyboard.write(x)
           time.sleep(4) #  here the time you want to spam .
           keyboard.send("enter")
    def main(self) :
           self.checkfile()
           self.spams()           
x = spam()  
x.main()       








