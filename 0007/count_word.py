import sys
import os
import re

PATH = "./"
words = {}
regex = re.compile('[^a-zA-Z]')

def main():
    path = os.listdir(PATH)
    print __file__
    print os.path.basename(sys.argv[0])
    # for filename in path:
    #     txt_name = PATH + filename
    #     try :
    #         input_txt = open(txt_name, 'r')
    #     except :
    #         print "Something Error"
        


    

if __name__=="__main__":
    main()
