import os
all_files = os.listdir('/data/Study/Major_Project/Bibliography_Tool/uploads')
for i in all_files:
    file = open("uploads/" + i, "r+")
    bib = file.read()
    print(bib)