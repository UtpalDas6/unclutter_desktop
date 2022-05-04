#Lets clean a cluttered desktop
from os import listdir
from os.path import isfile, join
import shutil, os
def clear_folder():
    mypath='C:\\Users\\udas\\Desktop'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file_name in onlyfiles:
        s=f.split('.')
        folder = s[1]
        path=mypath+'\\'+folder
        if not os.path.exists(path):
            os.mkdir(mypath+'\\'+folder)
        try:
            shutil.move(mypath+'\\'+file_name, mypath+'\\'+folder)
        except Exception as e:
            print(e)
    print('success')
