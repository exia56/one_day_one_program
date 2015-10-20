import sys
import os
import re

PATH = "0007/"
words = {}
regex = re.compile('[^a-zA-Z]')

def main():
    path = os.listdir(PATH)
    p = os.path.basename(sys.argv[0])
    for filename in path:
        if p in path:
            path.remove(p)
        txt_name = PATH + filename
        if os.path.isdir(txt_name):
            path.append(txt_name)

        #try :
        #    input_txt = open(txt_name, 'r')
        #except :
        #    print "Something Error"
    

def count_line_re():
    pass


    

if __name__=="__main__":
    main()
