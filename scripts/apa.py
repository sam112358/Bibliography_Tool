import os

def apa():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    all_files = os.listdir(dir_path + '/..' + '/uploads')
    for curr_file in all_files:
        bibtex = open("../uploads/" + curr_file, "r+")
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


        #Formatting

        #APA
        formatting = ''


        #1 Author
        names = elements['author']
        for i in names[:-1]:
            first_name = i[0][:1]
            last_name = i[1]
            curr_name = last_name + ', ' + first_name + '., '
            formatting += curr_name


        first_name = names[-1][0][:1]
        last_name = names[-1][1]
        curr_name = '& ' + last_name + ', ' + first_name + ', '
        formatting += curr_name


        #2 Year
        if 'year' in elements:
            formatting += '(' + elements['year'] + ')' + '. '

        #3 Title
        if 'title' in elements:
            formatting += elements['title'] + '. '

        #4 Booktitle or Publisher
        try:
            formatting += 'In ' + elements['booktitle'] + ' ' 
        except:
            pass

        #5 Volume
        try:
            formatting += ', ' + elements['volume']
        except:
            pass

        #6 Number
        try:
            formatting += '(' + elements['number'] + ')'
        except:
            pass

        #7 Pages
        try:
            formatting += ', (pp. ' + elements['pages'] + '). '
        except:
            pass

        #8 Organization
        try:
            formatting += elements['organization'] + '.'
        except:
            pass

        print(formatting)

apa()