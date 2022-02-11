import os
import shutil 

#Copy .txt



def convert():
    path = "output.txt"
    path2 = "command.txt"
    shutil.copy(path, path2)
    path = "command.txt"
    base = os.path.splitext(path)[0]
    try:
        os.rename(path, base + '.nc')
    except:
        os.remove("command.nc")
        os.rename(path, base + '.nc')


#convert()
