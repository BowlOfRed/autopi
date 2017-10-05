#!/usr/bin/python3
import sys
import os

#Given an image name and a directory, unpacks the raspbian image
#into the directory

if (len(sys.argv) != 3):
  sys.exit("Usage: %s [image] [respository]" % sys.argv[0])

image,repository = sys.argv[1:3]
print("image: %s repo: %s" % (image,repository))

if (not os.path.exists(image)):
  sys.exit("%s: Image path %s does not exist." % (sys.argv[0], image))

if (os.listdir(repository)):
  print ("Directory %s has files inside" % repository)
else:
  print ("Directory %s has no files" % repository)

  
