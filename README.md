# NTUC_Assignment

# Folders
**Images** - Stores histogram images

**Data** - Stores Zipped files and unzipped files extracted

**Note:**<br />
The python scripts will switch between main outer folder, Images and Data Folder when neccessary using python OS module
to perform required tasks.

# Scripts
download_files.py - Used for extracting zip files from website and unzipping them in **Data** folder. User need to specify website name and files.


### Example of website as unit test
```
https://archive.ics.uci.edu/ml/machine-learning-databases/00222/
```
### Example of files as unit test
```
bank-additional.zip, bank.zip
```

computation.py - processing logic for querying data and data visualisation. 
It saves plotly image too in **Images** folder.


# Requirements
It shows various importable python modules needed to download.

```
kaleido-0.2.1
numpy
pandas 
plotly
sqlite3
zipfile36
wget
kaleido
```



