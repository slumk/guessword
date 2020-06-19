# you can add words for playing guessword game using this python script
# use 'python add_words.py <your supposed word>
# you can add many words as you want
# beware of duplicatons,but it doesn't matter by the way



import sys

new_words=[]
for i in sys.argv[1:]:
        new_words.append(i)
with open('word_list.txt','a') as updated_word_file:
    for j in new_words:
        updated_word_file.write(j)
        updated_word_file.write("\n")
