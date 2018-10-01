Stir filenames
==============

This script will take two or more paths,
and randomly rotate the files between them.

No checks are made before proceeding.

Assuming everything goes well, each file will have moved;
files never end up with the same name they started with.

In the case of an error (such as permissions), no data should be lost;
files may or may not have been moved,
but there will likely be one file left in a temporary directory.
That temporary directory will be in the same location
as the first file in the originally-passed list,
and if it contains anything, it will be that same first file.

Why?
----

No idea. [Someone was asking for it on Reddit][reddit].

[reddit]: https://www.reddit.com/r/Doesthisexist/comments/9icuxe/a_program_that_randomizes_file_names/

Requirements
------------

- [Python](https://www.python.org/) 2 (2.7 might be required) or 3

You already have a suitable version of Python if you're on Mac OS X.

Usage
-----

This can be used from the command line, such as

    ./stir-filenames.py file1 file2 /tmp/file3 ~/file4

or

    ./stir-filenames.py /path/to/photos/*.jpg

...in which case information about which files were moved where,
and on any errors, is printed to the console.

Alternatively, some operating systems may allow files to be dragged to it.

- **Gnome desktop environment**: files can be dragged and dropped
  on the provided desktop entry
  (which at present expects to be in the same directory as the script)
- **Windows**: from what I can tell, some versions of Python on Windows already
  support dropping files on to scripts, so try it:
  drop files you want to stir on to the `stir-filenames.py` file.
  If it won't let you, try making a shortcut to the `stir-filenames.py` file
  (alt-drag) and try dropping files on to that.
  If that won't work either, run the provided `python-drop.reg` file
  to add a drop handler for Python files,
  then dropping on the script should work.
  [See a screenshot](https://i.imgur.com/QDqBweW.png).
- **Mac OS X**: I haven't tested, but it looks like
  [Dropscript][dropscript-info] (which is [available here][dropscript-dl])
  should help.

[dropscript-info]: http://www.wsanchez.net/papers/DropScript/
[dropscript-dl]: (http://www.wsanchez.net/software/

Warning
-------

Though I don't think this can cause any data loss
(except obviously knowledge of which file was originally which,
if you're not capturing the output),
no guarantees!
