# this script contains the base entities required for all of this game's source files.
# enjoy the game!!
# it's my first python attempt
# curently the words for guessing is limited.you can add it using add_words.py script

import random

ENG_CHARS="abcdefghijklmnopqrstuvwxyz"


file_for_test=open("word_list.txt",'r')
words_for_check = file_for_test.readlines()
lucky_word=random.choice(words_for_check).strip()
del words_for_check
file_for_test.close()
playing_list=list('_'*len(lucky_word))
if len(lucky_word)>5:
    fir_word=random.choice(lucky_word)
    sec_word=random.choice(lucky_word)
    playing_list[lucky_word.index(fir_word)]=fir_word
    playing_list[lucky_word.index(sec_word)]=sec_word
else:
    word=random.choice(lucky_word)
    playing_list[lucky_word.index(word)]=word
