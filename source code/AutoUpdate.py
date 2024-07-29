print("Updater V2, credit to: (discord) sania212")
import githubdl
import os
try:
    githubdl.dl_file("https://github.com/HOMENYK/Redactor-python-", "Main.exe", "Main_temp.exe", github_token="...")
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
else:
    if(str(input("Update found, are you want to install update? (T or F): ")) == "T"):
        F1 = open("Main.exe", "w+", encoding='utf-8')
        F1.write(Git_code)
        F1.close()
        print("Restart Redactor to see changes")
    else:
        print("Deleting changes...")
os.remove("Main_temp.exe")
Mfile.close()