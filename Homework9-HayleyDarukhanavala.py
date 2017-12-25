

def make_backwards_phonebook(phbook_file,back_phbook_file):
    new_book = {}
    phone_book = open("phone_numbers.tsv","r")
    book_data = phone_book.read()
    data_split = book_data.split("\n")
    new_book.write(data_split)
  

  
    book = {"Bugs Bunny": "301-123-4567",
            "Elmer Fudd": "212-777-8888",
            "Pippi Longstocking": "212-111-2222",
            "Under Dog": "203-999-1111"}
  


def user_input_make_bw_phonebook():
    input_file = input("Enter an input filename")
    output_file = input("Enter an output filename")
    
   
    







    


def holiday_dictionary():
    my_dictionary = {"Christmas":"12/25/2016",
                     "Halloween":"10/31/2016",
                     "Thanksgiving":"11/24/2016",
                     "Easter":"3/27/2016",
                     "Hannukah":"12/24/2016",
                     "Ramadan":"6/6/2016",
                     "Kwanza":"12/26/2016",
                     "Diwali":"10/30/2016"}
    
    list = [ ]
    string = "I wish you a merry Christmas"
    sentence_split = string.split(' ')
    list.append(sentence_split)
    print(list)
    
    for item in list:
        for word in item:
            if word in my_dictionary.keys():
                date = print(my_dictionary.get(word))
                list.append(date)
            else:
                list.append(word)



def word_count():
    import os
    text_file = open("read_it.txt", "r")
    text_file.close()
    text_file.open()
print(text_file.read())

word_count()




def word_count_file(infile, outfile):
    import os
    word_count = {}
    with open(infile, 'r') as instream:
        for word in instream.read():
            if word in word_count:
                word_count[word] = word_count[word] + 1

            else:
                word_count[word]=1

    with open(outfile, 'w') as outstream:









    
               
            
   
    
    
                     
                     






