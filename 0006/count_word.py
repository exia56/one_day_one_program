import sys
import os
import re

PATH = "txt/"
words = {}
regex = re.compile('[^a-zA-Z]')

def main():
    path = os.listdir(PATH)
    for filename in path:
        txt_name = PATH + filename
        try :
            input_txt = open(txt_name, 'r')
        except :
            print "Something Error"
        lines = input_txt.read().split()
        for word in lines:
            word = re.sub("\W", "", word)
            word = word.lower()
            if word.isalpha():
                words[word] = words.setdefault(word, 0) +1
                # if word in words:
                #     words[word] = words[word] + 1
                # else :
                #     words[word] = 1
    values = words.values()
    keys = words.keys()
    for i in range(10):
        while True:
            imax = max(values)
            idx = values.index(imax)
            key = keys.pop(idx)
            values.pop(idx)
            if len(key) > 5 or len(values) == 0:
                break
        print str(key) + " : " + str(imax)


    

if __name__=="__main__":
    main()
