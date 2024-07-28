print("Updater V1, credit to: (discord) sania212")

from requests import get
import os
try:
    Pastebin_code = get('https://pastebin.com/raw/DjaMavpR').text
except:
    print("Bad internet connection")
print("Checking for updates, please wait...")
Mfile = open("Main.py", "r", encoding='utf-8')
Current_code = Mfile.read()
Current_code = os.linesep.join([line for line in Current_code.splitlines() if line.strip() != ""])
Pastebin_code = os.linesep.join([line for line in Pastebin_code.splitlines()  if line.strip() != ""])
Current_code = Current_code.replace('\r\n', '\n')
Pastebin_code = Pastebin_code.replace('\r\n', '\n')

def check():
    F11 = open("1.txt", "w+", encoding='utf-8')
    F11.write(Current_code)
    F11.close()
    F21 = open("2.txt", "w+", encoding='utf-8')
    F21.write(Pastebin_code)
    F21.close()
if(Pastebin_code == Current_code):
    print("Your version already up to date")
else:
    if(str(input("Update found, are you want to install update? (T or F): ")) == "T"):
        F1 = open("Main.py", "w+", encoding='utf-8')
        F1.write(Pastebin_code)
        F1.close()
        print("Restart Redactor to see changes")
    else:
        print("Deleting changes...")

Mfile.close()