import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

#================encrypt==================
def encrypt(m,k):
    """
    for encrypt msg based on upper case or lower case 
    """
    cipher=""
    ofset_upper , ofset_lower = 65 , 97
    for char in m:
        char_num = ord(char)
        if char.isupper():
            shi_num = char_num+k - ofset_upper
            mod_num = shi_num % 26 + ofset_upper
            cipher += chr(mod_num)
        elif char.islower():
            shi_num = char_num+k - ofset_lower
            mod_num = shi_num % 26 + ofset_lower
            cipher += chr(mod_num)
        else:
            cipher += char         
    return cipher
#===============decrypt===================
def decrypt(d,k):
    """
    for decrypt msg
    """
    return encrypt(d,-k)

#===============count_words===================
def count_words(text):
    words_split = text.split()
    word_counter = 0

    for sp_word in words_split:
        word = re.sub (r'[^A-Za-z]+','', sp_word)
        if word.lower() in word_list or word in name_list:
            word_counter += 1
    return word_counter
#=====================cracks======================
def crack(en_text):
    text_length=len(en_text)
    for i in range (text_length):
        check_dec = decrypt(en_text,i)
        word_count=count_words(check_dec)
        percentage = int(word_count / len(en_text.split())*100)

        if percentage > 50:
            precent_result = check_dec
        
    return precent_result

if __name__ == "__main__":
    # input_txt = encrypt("It was the best of times, it was the worst of times",7)
    # print(input_txt)
    # decr_txt=decrypt( input_txt, 2)
    # print(decr_txt)
    # counter_word=count_words("It was the best of times, it was the worst of times")
    # print(counter_word)
    # counter_word=count_words(decr_txt)
    # print(counter_word)
    # print(crack(decr_txt))

    # input_txt = encrypt("Lab18 In Level401 pyThon",3)
    # print(input_txt)
    
    # input_txt = encrypt("THIS CODE SHOULD HANDLE UPPER CASE",3)
    # print(input_txt)

    # input_txt = encrypt("this code should handle lower case",3)
    # print(input_txt)
#incrept
    input_txt = encrypt(" It was the best of times, it was the worst of times.")
    print(input_txt)


    #===========================
    # input_txt = crack(" It was the best of times, it was the worst of times.")
    # print(input_txt)





    # It was the best of times, it was the worst of times.