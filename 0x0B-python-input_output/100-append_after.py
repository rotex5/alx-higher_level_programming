#!/usr/bin/python3
"""Module Incudes `append_after` function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """

    with open(filename, "r+", encoding="utf-8") as a_file:
        new_file = ""
        for line in a_file:
            new_file += line
            if search_string in line:
                new_file += new_string
        a_file.seek(0)
        a_file.write(new_file)
