
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
first_author = names_split[0].split(', ')
names_split.remove(names_split[0])
for i in range(len(names_split) - 1):
    names_split[i] = names_split[i].split(', ')
    names_split[i][0], names_split[i][-1] = names_split[i][-1], names_split[i][0]
elements['author'] = names_split

print(elements)


#Formatting

#APA
formatting = ''


#1 Author
names = elements['author']
formatting += first_author[0] + ', ' + first_author[1] 
if len(names) != 0:
    formatting += ', '
for i in names[:-1]:
    first_name = i[0]
    last_name = i[1]
    curr_name = first_name + ' ' + last_name + ', '
    formatting += curr_name


curr_name = names[-1].split(', ')
first_name = curr_name[0]
last_name = curr_name[1]
curr_name = 'and ' + first_name + ' ' + last_name + '. '
formatting += curr_name


#2 Title
if 'title' in elements:
    formatting += '"' + elements['title'] + '." '

#4 Booktitle or Publisher
try:
    formatting += elements['booktitle'] + ' ' 
except:
    pass
try:
    formatting += elements['journal'] + ' '
except:
    pass

#5 Volume
try:
    formatting += elements['volume']
except:
    pass

#6 Number
try:
    formatting += ' no. ' + elements['number'] + ' '
except:
    pass

#6 Year
try:
    formatting += '(' + elements['year'] + ')' 
except:
    pass

#7 Pages
try:
    formatting += ': ' + elements['pages']
except:
    pass


print(formatting)