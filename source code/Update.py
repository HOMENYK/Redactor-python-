import os
import githubdl
#Updater V3, credit to: (discord) sania212
print("Updater V3, credit to: (discord) sania212")
try:
    githubdl.dl_file("https://github.com/HOMENYK/Redactor-python-", "Main.exe", "Main_temp.exe", github_token="1234567890123456789012345678901234")
except:
    print("Bad internet connection")
print("Checking for updates, please wait...")
Mfile = open("Main.exe", "rb")
Current_code = Mfile.read()
Mfile.close()
Mfile2 = open("Main_temp.exe", "rb")
Git_code = Mfile2.read()
Mfile2.close()
if(Git_code == Current_code):
    print("Your version already up to date")
    os.remove("Main_temp.exe")
else:
    if(str(input("Update found, are you want to install update? (T or F): ")) == "T"):
        os.remove("Main.exe")
        os.rename("Main_temp.exe", "Main.exe")
        os.system("Main.exe")
    else:
        os.remove("Main_temp.exe")