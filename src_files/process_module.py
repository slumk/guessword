
import base_module
import sys

chars=base_module.ENG_CHARS
obf_word=[]
obf_word=base_module.playing_list
tried_chars=[]
def accept_move(char):
    if len(char) > 1:
        return "exceed"
    if char is None:
        return None
    if char.lower() in chars:
        if char in base_module.lucky_word:
            obf_word[base_module.lucky_word.index(char)]=char
            return obf_word
        else:
            if char not in tried_chars:
                tried_chars.append(char)
                return "notright"
            else:
                return "exnotright"
    else:
        return "NotAChar"

