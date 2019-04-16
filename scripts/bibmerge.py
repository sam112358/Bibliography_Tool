import os

dir_path = os.path.dirname(os.path.realpath(__file__))
all_files = os.listdir(dir_path + '/..' + '/uploads')

for i in all_files:
    file = open("../uploads/" + i, "r+")
    bib = file.read()
    print(bib)