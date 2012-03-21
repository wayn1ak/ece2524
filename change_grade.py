#!/usr/bin/env python

import re
import fileinput

verbose=False

def change_grade(user_input):

	result = ""	
	for line in user_input:
	    m = re.search(argv[1], line)
	    values = line.split(',') #note that split accepts an optional parameter to define what character the string is split on. If none is provided it defaults to any whitespace character
	    if m:
	        if verbose:
	            stderr.write("%r\n" % values)
	        values[3] = "%d\n" % float(argv[2])

	    result += ",".join(values)
	return result

if __name__=='__main__':
	from sys import stdin,stderr,stdout,argv,exit
	if len(argv) != 3:
	    stderr.write("Usage: change_grade.py STRING VALUE\n")
	    exit(1)
	result = change_grade(stdin)
	stderr.write(result) 
