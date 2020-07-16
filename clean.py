#!/usr/bin/env python

import os
import shutil
import sys

# Check if directory to be cleanup provided in command line arguments
# Else take current command line path as a default root directory path
if len(sys.argv) > 1:
    rootDir = sys.argv[1]
else:
    rootDir = os.getcwd()

# Defined directory to be removed
rmDirs = ["build", ".gradle", ".settings", ".cxx", ".idea", ".externalNativeBuild"]

# Defined file extensions to be removed
rmFiles = '.iml'

# Iterate to Root Directory
for root, subDirs, files in os.walk(rootDir):
    for dir in subDirs:
        if dir in rmDirs:
            try:
                shutil.rmtree(os.path.join(root, dir))
                print("Delete Directory: " + os.path.join(root, dir))
            except FileNotFoundError as err:
                # Print error and continue
                print(err)
                print("Delete Failed: " + os.path.join(root, dir))

    for file in files:
        if file.endswith(rmFiles):
            try:
                os.remove(os.path.join(root, file))
                print("Delete File: " + os.path.join(root, file))
            except FileNotFoundError as err:
                # Print error and continue
                print(err)
                print("Delete Failed: " + os.path.join(root, file))
