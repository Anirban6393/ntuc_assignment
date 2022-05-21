# NTUC_Assignment

**MLENG-Assignment.pdf**<br /> 
It tells us overall requirements for this assignment for both coding section and logical reasoning section 2.

## Folders
**Images** - Stores histogram images

**Data** - Stores Zipped files and unzipped files extracted

**Note:**<br />
The python scripts will switch between main outer folder, Images and Data Folder when neccessary using python OS module
to perform required tasks.

# SQL Scripts
There are separate sql scripts for creating and deleting tables that is called by computation.py script

# Transformer Module Scripts
**download.py:** <br />
It contains functions for extracting zip files from website and unzipping them in **Data** folder.

**data_ingestion.py:**<br />
This file detects all csv files in data directory and ingests them into a pandas dataframe and also has functions for connecting to a database,
creating and deleting tables from external sql script instead of having to hardcode sql commands in string within file itself.


# Main Running Scripts
### Downloading
download_files.py - Used for extracting zip files from website and unzipping them in **Data** folder. It invokes ```download.py```
script from ```transformer``` module. User need to specify website name and files.

```
python download_files.py
```

### Example of website as unit test<br /> 
User to provide website name where file to be downloaded from.
```
https://archive.ics.uci.edu/ml/machine-learning-databases/00222/
```
### Example of files as unit test<br /> 
This user arguement advices user to provide multiple file names in a website which will be stored in a list
for iterating and unzipping.

```
bank-additional.zip,bank.zip
```

### Computation
computation.py - processing logic for querying data and data visualisation. <br />
This script invokes ```data_ingestion.py``` from transformer module for creating tables via DDL statements and ingesting all detected csv files
into pandas dataframe called customers that will be inserted into a sqlite table.

It saves plotly image too in **Images** folder. <br />
It will also display a table that shows percentage breakdown of people for each occupation.

Uses list comprehension to detect all csv files and append iteratively to single dataframe called **customers**.
## Requirements File
The following command will install the packages according to the configuration file requirements.txt.
```
$ pip install -r requirements.txt
```
The ```requirements.txt``` file shows various importable python modules needed to download.
```
kaleido
numpy
pandas 
plotly
sqlite3
zipfile36
wget
kaleido
```

## Section 2
**Software Engineering Questions.txt** 
This text file contains answers to section 2 of the pdf document. I explained mathematicall approaches, suggested some common data services in cloud and choice of data to collect and display in the form of tables for querying.

