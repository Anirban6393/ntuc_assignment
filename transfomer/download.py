import wget
import os
from zipfile import ZipFile



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