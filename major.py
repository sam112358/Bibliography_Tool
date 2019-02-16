
bibtex = open("bib.bib","r+")

file = bibtex.read()
elements = {}
j = 0


iden = ''
while(file[j] != ","):
    iden += file[j]
    j += 1
j += 1
i = j


while i in range(len(file)): 
    col_name = ''
    col_data = ''
    try:
        while(file[i] != '='):
            col_name += file[i]
            i += 1
        i += 2
    except:
        pass

    try:
        while(file[i] != '}'):
            col_data += file[i]
            i += 1
        i += 2
    except:
        pass
    

    col_name = col_name[3:]
    elements[col_name] = col_data
    
iden = iden.split('{')
elements['id'] = iden[1]
elements.pop('')

names_split = elements['author'].split(' and ')
for i in range(len(names_split)):
    names_split[i] = names_split[i].split(', ')
    names_split[i][0], names_split[i][-1] = names_split[i][-1], names_split[i][0]
elements['author'] = names_split

print(elements)