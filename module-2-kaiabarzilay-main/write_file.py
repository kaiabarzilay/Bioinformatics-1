#!/usr/bin/env python
# write_file.py
line_to_write = 'some text to write to the file'
filename = "out_file.txt"  # just the name of the file I'm going to write

# Open the file, and pass the 'w' parameter which means write to the file.
with open(filename, 'w') as out:
    # Write the line of output
    out.write(line_to_write)
