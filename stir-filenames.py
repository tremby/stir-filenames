#!/usr/bin/env python

from __future__ import print_function

import os
import random
import tempfile
import sys

# Make sure we were given at least two filenames
if len(sys.argv) < 3:
    print("Expected at least two filenames as arguments", file=sys.stderr)
    sys.exit(1)

# Get list of filenames
filenames = sys.argv[1:]

# Randomize their order, but keep the originally-first filename at the start
# This is so if something goes wrong, it's predictable which file is left in a
# temporary directory (the first one passed in)
first_filename = filenames[0]
other_filenames = filenames[1:]
random.shuffle(other_filenames)
filenames = [first_filename] + other_filenames
del first_filename
del other_filenames

# Make a temporary directory near the first file
temp_dir = tempfile.mkdtemp(dir=os.path.dirname(filenames[0]))
temp_file = os.path.join(temp_dir, os.path.basename(filenames[0]))

class HandledError(RuntimeError):
    pass

try:
    # Loop through all files, moving them to the location of the previous file
    for index, filename in enumerate(filenames):
        source = filename

        # Set the destination as the original name/location of the previous file
        # in the list, or the temporary location in the case of the first file
        destination = temp_file if index == 0 else filenames[index - 1 % len(filenames)]

        # Move the file
        try:
            os.rename(source, destination)
            print("'%s' -> '%s'" % (source, destination))
        except OSError as e:
            print("Failed to move '%s' -> '%s': %s"
                    % (source, destination, e), file=sys.stderr)
            raise HandledError(e)

    # Move the first file from its temporary location to its destination
    print("'%s' -> '%s'" % (temp_file, filenames[len(filenames) - 1]))
    os.rename(temp_file, filenames[len(filenames) - 1])

except HandledError:
    sys.exit(1)

finally:
    # Remove the temporary directory
    try:
        os.rmdir(temp_dir)
    except OSError:
        print("The first file (%s) has been left in this temporary directory: %s"
                % (filenames[0], temp_dir), file=sys.stderr)
