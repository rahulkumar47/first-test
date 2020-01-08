import os
import shutil

path = "C:\Users\ROHIT\Desktop\path"
names = os.listdir(path)
folder_name = ['image','pdf']
for x in range(0,2):
   if not os.path.exists(path+folder_name[x]):
          os.makedirs(path+folder_name[x]):
         
for files in name:
     if "jpg" in files and not os.path.exists(path+'image\'+files):
    shutil.move (path+files, path+'image\'+files):

if "pdf" in files and not os.path.exists(path+'pdf\'+files):
    shutil.move (path+files, path+'pdf\'+files):
