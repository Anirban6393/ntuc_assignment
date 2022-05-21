import os
from download import *

os.chdir((os.getcwd()+'\\data'))

if __name__ == "__main__":
    #specify website name
    print('Website name:')
    website=input()
    print('File names to download:')
    #files=['bank-additional.zip','bank.zip']
    files = list(map(str, input("Enter multiple file names: ").split(',')))
    print("List of files: ", files)
    file_directory=[website+file for file in files]
    current_dir=[(os.getcwd()+'/').replace('\\','/')+file for file in files]
    [download_files(file) for file in file_directory]
    [unzip_files(file) for file in current_dir]
    

