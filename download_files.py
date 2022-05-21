import wget
import os
from zipfile import ZipFile

os.chdir((os.getcwd()+'\\data'))

def download_files(url:str):
    link=url
    wget.download(link)

  
def unzip_files(file:str):
    # opening the zip file in READ mode
    with ZipFile(file, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Downloaded {}!'.format(file))

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
    

