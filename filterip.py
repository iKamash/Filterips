#!/usr/bin/env python3
# remove a line containing a string
import time
import os.path
from os import path



file_name = input('Enter Your File : ')


if path.exists(file_name):
  pass
else:
  print('I CANT SEE IT , it must be in the same direcotry ')
  exit()



word = '.'

with open(file_name,'r') as file:
    lines = file.readlines()

with open(file_name,'w') as file:
    for line in lines:
        # find() returns -1 if no match is found
        # if line.find(word) == -1: # if not -1 that meen he didnt found the substing
        if word in line:
          file.write(line)
        else:
            pass
            # pass