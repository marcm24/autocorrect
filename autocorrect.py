# taking file names
dict_file = input('Dictionary file => ')
print(dict_file)
input_words = input('Input file => ')
print(input_words)
keyboard_file = input('Keyboard file => ')
print(keyboard_file)

# opening the files
dict_open = open(dict_file, encoding = 'utf8')
input_open = open(input_words, encoding = 'utf8')
keyboard_open = open(keyboard_file, encoding = 'utf8')

# going through the dictionary file, and making a dictionary of the words as keys, with the frequencies as values
dictionary = dict() 
for line in dict_open: # words_10percent.txt
    line = line.split(',')
    dictionary['{}'.format(line[0])] = float(line[1])
 
# going through the keyboard file, and making a dictionary of each letter as keys, with the neighboring keys as values
keyboard_dict = dict()
for line in keyboard_open: # keyboard.txt
    line = line.split()
    first_letter = line[0]
    line.remove(first_letter)
    keyboard_dict[first_letter] = line
  
# making a list of the input words
words_list = []
for line in input_open: # input_words.txt
    words_list.append(line)

# remove the \n from the words
good_words_list = []
for w in words_list:
    if '\n' in w:
        word = w.replace('\n', '')
        words_list.insert(words_list.index(w), word)
        words_list.remove(w)
   
# make a list of the dictionary words by making a list of the keys
dictionary_words = list(dictionary.keys())
# make a list of the dictionary values/frequencies by making a list of the values
dictionary_values = list(dictionary.values())

# make a list of the keyboard keys by making a list of the keys
keyboard_keys_list = list(keyboard_dict.keys())
# make a list of the neighboring keys by making a list of the values
keyboard_values_list = list(keyboard_dict.values())

# list of all letters for insert check
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# functions for each of the checks

# drop function, drops each letter of the word
def drop(word):
    string_list = []
    for i in word:
        string_list.append(i) # make a list of the word split into letters
    
    c = 0
    dropped_list = []
    while c < len(string_list): # runs through the list and deletes each index of the list, and joins the list to append to a list of dropped words
        letter = string_list[c]
        del string_list[c]
        joined_word = ''.join(string_list) 
        dropped_list.append(joined_word) # must revert back to original word to check with next
        string_list.insert(c, letter)
        c += 1
        dropped_list = list(set(dropped_list)) 
        
    return dropped_list

# insert function, inserts all letters from alphabet to each position of the word
def insert(word):
    letter_list = []
    for i in word:
        letter_list.append(i) # make a list of the word split into letters
           
    inserted_list = []
    z = 0
    while z < len(alphabet): # run through each letter of the alphabet
        i = 0
        while i <= len(word): # run through each position of the word, including the last, and insert into the index of the iterable, the index of the alphabet list z, which is the letter we are searching thorugh
            letter_list.insert(i, alphabet[z])
            inserted_list.append(''.join(letter_list))
            del letter_list[i]
            i += 1
        z += 1
    return inserted_list

# swap function, swaps every 2 consecutive letters (by position)
def swap(word):
    split_word = []
    for i in word:
        split_word.append(i) # make a list of the word split into letters


    swapped_list = []
    i = 0 
    while i < len(split_word):
        if i + 1 == len(split_word):
            break
        letter_1 = split_word[i]
        letter_2 = split_word[i + 1] # record the letters we are swapping

        del split_word[i]
        del split_word[i] # delete the 2 letters which we are swapping
    
        split_word.insert(i, letter_1)
        split_word.insert(i, letter_2) # insert the 2 letters in reverse order
    
        swapped_list.append(''.join(split_word)) # add the joined swapped list to a new list
    
        del split_word[i]
        del split_word[i] # delete the 2 swapped letters
         
        split_word.insert(i, letter_2)
        split_word.insert(i, letter_1) # insert back in the original order
        
        i += 1   
    return swapped_list

# replace function, replaces every letter in the word by their neighboring keyboard letter
def replace(word):
    words_list = [] 
    for i in word:
        words_list.append(i) # make a list of the word split into letters 

    replaced_list = []
    p = 0
    while p < len(words_list): # run through the word
        q = 0
        original_letter = words_list[p]
        key_index = keyboard_keys_list.index(original_letter) # record the original letter, and the index of it
        while q < len(keyboard_values_list[key_index]): # run through the values of the letter we are replacing from the keyboard dictionary
            replacing_letter = keyboard_values_list[key_index][q]
            del words_list[p]
            words_list.insert(p, replacing_letter)
            replaced = ''.join(words_list)
            replaced_list.append(replaced)
            del words_list[p]
            words_list.insert(p, original_letter)    # record the replacing letter, delete the original, insert each of the replaced and record it to a list. revert back to the original for the next test.
            q += 1
        p += 1
    return replaced_list


for word in words_list: # run through our words list and see if any are initially in the dictionary
    word = word.strip()
    test_words = []
    if word in dictionary_words:
        print('{} -> FOUND'.format(word.rjust(15, ' ')))
    elif word not in dictionary_words: # if they are not, run the tests
# ////////////////////////////////////////////////////////////////////////////       
       # dropping each letter
       
       dropped = drop(word)
       for i in dropped: # see if the words produced are in the dictionary
           if i in dictionary_words:
               test_words.append(i)
        
# //////////////////////////////////////////////////////////////////////////// 
       # insert letter
        
       inserted = insert(word)
       for i in inserted: # see if the words produced are in the dictionary
           if i in dictionary_words:
               test_words.append(i)
# ////////////////////////////////////////////////////////////////////////////
       # swap letter

       swapped = swap(word)
       for i in swapped: # see if the words produced are in the dictionary
          if i in dictionary_words:
              test_words.append(i)
# ////////////////////////////////////////////////////////////////////////////
       # replace letter from keyboard dict
       
       replaced = replace(word)
       for i in replaced: # see if the words produced are in the dictionary
           if i in dictionary_words:
               test_words.append(i)
# ////////////////////////////////////////////////////////////////////////////
       # sorting by frequency
       
       frequencies = []
       for i in test_words:
           index = dictionary_words.index(i)
           if len(test_words) > 1:
               frequencies.append(((dictionary_values[index]), i))
           frequencies = sorted(frequencies, reverse = True) # make a tuple of the frequency, and the word and sort by highest to low
           
           words_by_frequency = []
           for i in frequencies:
               words_by_frequency.append(i[1]) # make a list of the second item in the tuple, which is the word
# ////////////////////////////////////////////////////////////////////////////
       # final printing
       
       if len(test_words) > 0:
           if len(test_words) == 1: # print the test list as it is only 1 item
               print('{} -> FOUND  {}:  {}'.format(word.rjust(15, ' '), len(test_words), test_words[0]))
           elif len(test_words) >= 3 and len(test_words) < 10:
               print('{} -> FOUND  {}:  {} {} {}'.format(word.rjust(15, ' '), len(test_words), words_by_frequency[0], words_by_frequency[1], words_by_frequency[2]))
           elif len(test_words) >= 10:
               print('{} -> FOUND {}:  {} {} {}'.format(word.rjust(15, ' '), len(test_words), words_by_frequency[0], words_by_frequency[1], words_by_frequency[2]))
           else: # print out the words_by_frequency as it is a sorted list of multiple words
               print('{} -> FOUND  {}:  {}'.format(word.rjust(15, ' '), len(test_words), str(words_by_frequency).strip('[]').replace(',' ,'').replace('\'', '')))
       else: # if not, just print not found
           print('{} -> NOT FOUND'.format(word.rjust(15, ' ')))