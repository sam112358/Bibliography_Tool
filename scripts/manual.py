import os

def manual():
    all_files = os.listdir('/data/Study/Major_Project/Bibliography_Tool/uploads')
    for curr_file in all_files:
        bibtex = open("uploads/" + i, "r+")

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
        #1
        ## First Name, Last Name
        names = elements['author']
        for i in names[:1]:
            first_name = i[0]
            last_name = i[1]
            curr_name = first_name + ', ' + last_name + ', '
            formatting += curr_name

        first_name = names[-1][0]
        last_name = names[-1][1]
        curr_name = '& ' + first_name + ', ' + last_name + ', '
        formatting += curr_name


        ## Last Name, First Name
        names = elements['author']
        for i in names[:1]:
            first_name = i[0]
            last_name = i[1]
            curr_name = last_name + ', ' + first_name + ', '
            formatting += curr_name

        first_name = names[-1][0]
        last_name = names[-1][1]
        curr_name = '& ' + last_name + ', ' + first_name + ', '
        formatting += curr_name


        ## F. Last Name
        names = elements['author']
        for i in names[:1]:
            first_name = i[0][:1]
            last_name = i[1]
            curr_name = first_name + '. ' + last_name + ', '
            formatting += curr_r i in names[:1]:
            first_name = i[0]
            last_name = i[1]
            curr_name = last_name + ', ' + first_name + ', '
            format   name

        first_name = names[-1][0][:1]
        last_name = names[-1][1]
        curr_name = '& ' + first_name + '. ' + last_name + ', '
        formatting += curr_name


        ## L. First Name
        names = elements['author']
        for i in names[:1]:
            first_name = i[0]
            last_name = i[1][:1]
            curr_name = last_name + '. ' + first_name + ', '
            formatting += curr_name

        first_name = names[-1][0]
        last_name = names[-1][1][:1]
        curr_name = '& ' + last_name + ', ' + first_name + ', '
        formatting += curr_name





        #2 Year
        ## Parenthesis with ,
        if 'year' in elements:
            formatting += '(' + elements['year'] + ')' + ','


        ## Inverted Commas with ,
        if 'year' in elements:
            formatting += '"' + elements['year'] + '"' + ','


        ## Parenthesis with .
        if 'year' in elements:
            formatting += '(' + elements['year'] + ')' + '.'


        ## Inverted Commas with .
        if 'year' in elements:
            formatting += '"' + elements['year'] + '"' + '.'






        #3 Title
        ## None with ,
        if 'title' in elements:
            formatting += elements['title'] + ', '


        ## None with .
        if 'title' in elements:
            formatting += elements['title'] + '. '


        ## () with ,
        if 'title' in elements:
            formatting += '(' + elements['title'] + ')' + ', '


        ## () with .
        if 'title' in elements:
            formatting += '(' + elements['title'] + ')' + '. '


        ## "" with ,
        if 'title' in elements:
            formatting += '"' + elements['title'] + '"' + ', '


        ## "" with .
        if 'title' in elements:
            formatting += '"' + elements['title'] + '"' + '. '






        #4 Booktitle
        ## None with ,
        if 'booktitle' in elements:
            formatting += elements['booktitle'] + ', '


        ## None with .
        if 'booktitle' in elements:
            formatting += elements['booktitle'] + '. '


        ## () with ,
        if 'booktitle' in elements:
            formatting += '(' + elements['booktitle'] + ')' + ', '


        ## () with .
        if 'booktitle' in elements:
            formatting += '(' + elements['booktitle'] + ')' + '. '


        ## "" with ,
        if 'booktitle' in elements:
            formatting += '"' + elements['booktitle'] + '"' + ', '


        ## "" with .
        if 'booktitle' in elements:
            formatting += '"' + elements['booktitle'] + '"' + '. '





        #5 Publisher
        if 'publisher' in elements:
            formatting += elements['publisher'] + ', '


        ## None with .
        if 'publisher' in elements:
            formatting += elements['publisher'] + '. '


        ## () with ,
        if 'publisher' in elements:
            formatting += '(' + elements['publisher'] + ')' + ', '


        ## () with .
        if 'publisher' in elements:
            formatting += '(' + elements['publisher'] + ')' + '. '


        ## "" with ,
        if 'publisher' in elements:
            formatting += '"' + elements['publisher'] + '"' + ', '


        ## "" with .
        if 'publisher' in elements:
            formatting += '"' + elements['publisher'] + '"' + '. '






        #6 Number
        ## None with ,
        if 'number' in elements:
            formatting += elements['number'] + ', '


        ## None with .
        if 'number' in elements:
            formatting += elements['number'] + '. '


        ## () with ,
        if 'number' in elements:
            formatting += '(' + elements['number'] + ')' + ', '


        ## () with .
        if 'number' in elements:
            formatting += '(' + elements['number'] + ')' + '. '


        ## "" with ,
        if 'number' in elements:
            formatting += '"' + elements['number'] + '"' + ', '


        ## "" with .
        if 'number' in elements:
            formatting += '"' + elements['number'] + '"' + '. '






        #7 Pages
        ## None with ,
        if 'pages' in elements:
            formatting += elements['pages'] + ', '


        ## None with .
        if 'pages' in elements:
            formatting += elements['pages'] + '. '


        ## () with ,
        if 'pages' in elements:
            formatting += '(' + elements['pages'] + ')' + ', '


        ## () with .
        if 'pages' in elements:
            formatting += '(' + elements['pages'] + ')' + '. '


        ## "" with ,
        if 'pages' in elements:
            formatting += '"' + elements['pages'] + '"' + ', '


        ## "" with .
        if 'pages' in elements:
            formatting += '"' + elements['pages'] + '"' + '. '






        #8 Organization
        ## None with ,
        if 'organization' in elements:
            formatting += elements['organization'] + ', '


        ## None with .
        if 'organization' in elements:
            formatting += elements['organization'] + '. '


        ## () with ,
        if 'organization' in elements:
            formatting += '(' + elements['organization'] + ')' + ', '


        ## () with .
        if 'organization' in elements:
            formatting += '(' + elements['organization'] + ')' + '. '


        ## "" with ,
        if 'organization' in elements:
            formatting += '"' + elements['organization'] + '"' + ', '


        ## "" with .
        if 'organization' in elements:
            formatting += '"' + elements['organization'] + '"' + '. '





        #8 Journal
        ## None with ,
        if 'journal' in elements:
            formatting += elements['journal'] + ', '


        ## None with .
        if 'journal' in elements:
            formatting += elements['journal'] + '. '


        ## () with ,
        if 'journal' in elements:
            formatting += '(' + elements['journal'] + ')' + ', '


        ## () with .
        if 'journal' in elements:
            formatting += '(' + elements['journal'] + ')' + '. '


        ## "" with ,
        if 'journal' in elements:
            formatting += '"' + elements['journal'] + '"' + ', '


        ## "" with .
        if 'journal' in elements:
            formatting += '"' + elements['journal'] + '"' + '. '


        print(formatting)