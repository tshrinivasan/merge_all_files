#-*- coding: utf-8 -*-

# Author : T Shrinivasan <tshrinivasan@gmail.com>
# Version : 1.0
# Description : A program to combine contents of all the  files from all the subdirectories of a given directory

import os
import sys
import time
import optparse


desc = """

This program combines contents of all the  files
from all the subdirectories of given directory.

"""

parser = optparse.OptionParser(description=desc, version='%prog version 1.0')
parser.add_option('-t', '--target', help='target folder to collect the files', dest='target')

(opts, args) = parser.parse_args()



if opts.target is None:
       print "\n Directory name is missing\n"
       parser.print_help()
       exit(-1)
                     

t = time.localtime()
timestamp = time.strftime('%d-%m-%Y_%H%M', t)

target_folder = opts.target
target_file = "./" + opts.target.split('/')[-1] + "_collected_" + timestamp + ".txt"


target = open(target_file,"a")
count = 1

for dirpath, dirnames, filenames in os.walk(target_folder):
    for filename in [f for f in filenames ]:
        filename = os.path.join(dirpath, filename)
        content = open(filename,'r')
        print "Collecting the content of the file ...  " + filename 
        for line in content:
            target.write(line)
        count = count + 1

content.close()
target.close()

print "\n"
print "\n"

print "Collected contents from " + str(count) + " files"
print "Stored all the content in " + target_file

print "\n"

print "Bye"

print "\n"
