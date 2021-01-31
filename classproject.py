import os
import glob
import shutil
import os


src_dir = "/Users/swatiahuja/Desktop" 
dst_dir = "/Users/swatiahuja/Documents"
for jpegfile in glob.iglob(os.path.join(src_dir, "*.jpeg")): #moves jpeg files
    shutil.copy(jpegfile, dst_dir)
os.system("open \"\" https://code.whitehatjr.com/s/dashboard")#opens most used websites
os.system("open \"\" https://mail.google.com")#opens most used websites
os.system("open \"\" https://github.com/")#opens most used websites
