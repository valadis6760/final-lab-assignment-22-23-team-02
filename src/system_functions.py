import sys
import os
from datetime import datetime

# reads all the files found at the dir_path input
def getFilesPathInDir(dir_path):
    files_names = []
    with os.scandir(dir_path) as entries:
        for entry in entries:
            ## files found in dir
            files_names.append(entry.path)
    return files_names

## use this function to include restricctions to the arguments inputs
def checkArguments():

    length = len(sys.argv)
    return sys.argv[1:(length)]

def createFile(path_file):
    fd = open (path_file, "wb")
    return fd

def writeStrInFile(path_file, str):
    fd = open (path_file, "a")
    fd.write(str)
    return

def get_date_time():
    dt = datetime.now()
    date = {'day':dt.day, 'month': dt.month, 'year': dt.year, 'hour': dt.hour, 'min': dt.minute, 'sec': dt.second}
    return date

def check_file_exist(path):
    ''' Return a bool True is file exist otherwise False'''
    return os.path.isfile(path)