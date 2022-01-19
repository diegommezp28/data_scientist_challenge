from os import listdir, rename, path, mkdir, walk, rmdir
from os.path import join, isfile
import os
import shutil
import pandas as pd

#Read Labels
labels = pd.read_csv('./labels.csv')
lables_indexes = labels.iloc[:,0]
labels.head().iloc[:,0]

#Create subfolders for each label
test_dir = './traffic_Data/TEST/'
for index, value in lables_indexes.items():
    label_dir_path = join(test_dir, str(value))
    mkdir(label_dir_path)

#Move TEST files to each subfolder
for filename in listdir(test_dir):
    if(isfile(join(test_dir, filename))):
        try:
            class_label = int(filename[0:3])
            rename(join(test_dir, filename), join(test_dir, str(class_label), filename))
        except:
            print(f'{filename} is not a TEST file')


#Remove empty folders
def remove_empty_folders(path_abs):
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(listdir(path)) == 0:
            rmdir(path)
            
remove_empty_folders(test_dir)
   