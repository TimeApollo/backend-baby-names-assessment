#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++

    with open(filename , 'r' ) as f:
        data = f.read()
    
    year = re.search(r'Popularity\sin\s(\d+)' , data)

    name_dict = {}
    name_list = [year.group(1)]

    names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>' , data)

    # [0] = rank; [1] = guy ; [2] = girl
    for name in names:
        if not name_dict.get(name[1]) or int(name_dict[name[1]] > int(name[0])):
            name_dict[name[1]] = name[0]
        if not name_dict.get(name[2]) or int(name_dict[name[2]] > int(name[0])):
            name_dict[name[2]] = name[0]

    for key in sorted(name_dict):
        name_list.append( key + ' ' + name_dict[key])

    return name_list

def create_sum_file( names , filename ):
    summary = filename + '.summary'

    with open( summary , 'w') as f:
        f.write(names)
    


def main():
    # This command-line parsing code is provided.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    create_summary = args.summaryfile

     # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    
    if create_summary:
        for file in file_list:
            name_list = extract_names(file)
            names = '\n'.join(name_list) + '\n'
            create_sum_file( names , file )
    else:
        for file in file_list:
            name_list = extract_names(file)
            print('\n'.join(name_list) + '\n')
    

if __name__ == '__main__':
    main()
