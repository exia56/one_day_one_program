from PIL import Image
import os

o_PATH = 'old/'
n_PATH = 'new/'
MAX_W = 720
MAX_H = 640

def main(*argv):
    for name in argv:
        filename = o_PATH+name
        inp = Image.open(filename)
        w, h =inp.size
        while w > MAX_W or h > MAX_H:
            if w > h:
                h = h / ( w / MAX_W )
                w = MAX_W
            else :
                w = w / ( h / MAX_H )
                h = MAX_H

        new_pic = inp.resize((w, h), Image.ANTIALIAS)
        newfn = n_PATH+name
        new_pic.save(newfn)

if __name__ == '__main__':
    argv = os.listdir(o_PATH)
    main(*argv)


