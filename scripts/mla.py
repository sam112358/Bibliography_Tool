import os

def mla():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    all_files = os.listdir(dir_path + '/..' + '/uploads')
    for curr_file in all_files:
        bibtex = open("../uploads/" + curr_file, "r+")
        file = bibtex.read()

        #print(file)

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

        #MLA
        formatting = ''

        #1 Name
        names = elements['author']
        if len(names) < 3:
            for i in names[:-1]:
                first_name = i[0]
                last_name = i[1]
                curr_name = last_name + ', ' + first_name + ', '
                formatting += curr_name

            first_name = names[-1][0]
            last_name = names[-1][1]
            curr_name = 'and ' + last_name + ', ' + first_name
            formatting += curr_name

        else:
            first_name = names[0][0]
            last_name = names[0][1]
            curr_name = last_name + ', ' + first_name + ', '
            formatting += curr_name
            formatting += 'et al. '

        #2 Paper title
        formatting += '. "' + elements['title'] + '." '

        #3 Booktitle + Journal
        if 'booktitle' in elements:
            formatting += elements['booktitle']

        if 'journal' in elements:
            formatting += elements['journal']

        formatting += '.'

        #4 Organisation or Publisher
        if 'organisation' in elements:
            formatting += elements['organisation']

        if 'publisher' in elements:
            formatting += elements['puiblisher']


        #
        if 'organization' in elements:
            formatting += ' ' + elements['organization'] + ','


        if 'year' in elements:
            formatting += ' ' + elements['year']


        print(formatting)

        #formatting += '"' + elements['title'] + '." ' #+ elements[booktitle] + '. ' + elements['organization']
        #print(formatting)


mla()