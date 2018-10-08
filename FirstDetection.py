import  tensorflow as tf

from PIL import Image
from imageai.Detection import ObjectDetection
import sys
import imageio
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

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel() #prediction_speed="fast"

images = []

for i in range(1,a):

   # if(i%10==0):
      #  i=i+1
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , 'a'+str(i)+".jpg"), output_image_path=os.path.join(execution_path , 'b'+str(i)+".jpg"))
    for eachObject in detections:
        print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
    images.append(imageio.imread('b'+str(i)+".jpg"))
print(images)
#for filename in filenames:
imageio.mimsave('output03.gif', images, duration=0.1)
#filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('  .jpg')))
#print(filenames)
