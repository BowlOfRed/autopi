#!/bin/python
import sys

#Given an image name and a directory, unpacks the raspbian image
#into the directory

if (len(sys.argv) != 3):
  sys.exit("Usage: %s [image] [respository]")

