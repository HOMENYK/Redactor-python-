import os
os.remove("Main.exe")
os.rename("Main_temp.exe", "Main.exe")
os.system("Main.exe")