import sys

def main():
    words={}
    try :
        txt_name = sys.argv[1]
        input_txt = open(txt_name, 'r')
    except :
        print "Something Error"
    lines = input_txt.read().split()
    for word in lines:
        if word.isalpha():
            if word in words:
                words[word] = words[word] + 1
            else :
                words[word] = 1

    for word, count in words.iteritems():
        print word, '\t' if len(word)>6 else '\t\t' ,count

if __name__=="__main__":
    main()
