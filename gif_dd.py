
from PIL import Image

import sys

import os
def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print ("Cant load", infile)
        sys.exit(1)
   # i = 10
    i=0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGB", im.size)
            new_im.paste(im)
          #  if(i%10==0):
          #      i=i+1
            new_im.save('a'+str(i)+'.JPG')

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence
    return i
a = processImage('piaoyi.gif')