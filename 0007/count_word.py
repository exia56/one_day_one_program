import sys
import os
import re

PATH = "./"
lines = 0
comment = 0
no_line = 0

def main():
    path = os.listdir(PATH)
    p = os.path.basename(sys.argv[0])
    if p in path:
            path.remove(p)
    for filename in path:
        if os.path.isdir(filename):
            path.extend( get_next_dir(filename) )
        elif os.path.isfile(filename) and filename[len(filename)-3:]==".py":
            check_lines(filename)
    print "lines = " + str(lines)
    print "no line = " + str(no_line)
    print "commen = " + str(comment)

def get_next_dir(filename):
    next_path = os.listdir(filename)
    path = []
    for p1 in next_path:
        pa = filename+"/"+p1
        path.append(pa)
    return path

def check_lines(filename):
    global no_line
    global lines
    global comment
    _file = open(filename)
    ll = _file.readlines()
    for l in ll:
        idx = 0
        while (l[idx] == ' '):
            idx = idx +1
        if l == '' or l[idx:] == '\n':
            no_line = no_line + 1
        elif l[idx] == '#':
            comment = comment + 1
        else : 
            lines = lines + 1

if __name__=="__main__":
    main()
