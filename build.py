#!/usr/bin/python3
# Build script for master documents

import os
import sys
import re

EXCLUDED_DIRS = [".git"]
DIRS = [x for x in os.listdir() if os.path.isdir(x) and not x in EXCLUDED_DIRS]

# Help menu
def print_help():
    print("USAGE: build.py 'NAME OF DIR'")
    print("Possible DIRS: ")
    for dir in DIRS:
        print(f">\t{dir}")


def read_contents_from_file(file_name):
    with open(file_name, "r") as reader:
        contents = reader.readlines()
    
    start_index = 0
    start_regex = re.compile(r"\\maketitle")
    end_index = 0
    end_regex = re.compile(r"\\end{document}")

    for index, line in enumerate(contents):
        if start_regex.search(line) is not None:
            start_index = index
        elif end_regex.search(line) is not None:
            end_index = index
    
    return contents[start_index+1:end_index]


# Start parsing and set global vars
if len(sys.argv) < 2:
    print_help()
    exit(1)
elif "--help" in sys.argv:
    print_help()
    sys.exit(0)
elif not sys.argv[1] in DIRS:
    print(f"ERROR: '{sys.argv[1]}' not a valid option")
    print_help()
    sys.exit(1)


SELECTED_DIR = sys.argv[1]
MASTER_FILENAME = f"{SELECTED_DIR}/master.tex"
IGNORE_FILENAMES = ["master.tex"]
tex_regex = re.compile(r"\.tex$")
COMPILE_FILENAMES = [f"{SELECTED_DIR}/{x}" for x in os.listdir(SELECTED_DIR) if tex_regex.search(x) is not None and not x in IGNORE_FILENAMES]
COMPILE_FILENAMES.sort()

# Read file
with open(MASTER_FILENAME, "r") as reader:
    contents = reader.readlines()

head = []
maketitle_regex = re.compile(r"\\maketitle")
feet = []
end_regex = re.compile(r"\\end{document}")

for index, line in enumerate(contents):
    if maketitle_regex.search(line) is not None: # \maketitle found
        head = contents[:index+1]
    elif end_regex.search(line) is not None:
        feet = contents[index:]


contents = []
print(COMPILE_FILENAMES)
for file_name in COMPILE_FILENAMES:
    contents += read_contents_from_file(file_name)


with open(MASTER_FILENAME, "w") as writer:
    writer.writelines(head)
    writer.writelines(contents)
    writer.writelines(feet)

