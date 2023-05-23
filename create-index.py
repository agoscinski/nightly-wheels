#!/usr/bin/env python
import glob
import os
import sys

HTML_START = """<!DOCTYPE html>
<html>
  <body>
"""

HTML_END = """
  </body>
</html>
"""


def error(message):
    print("error:", message, file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        error(f"usage: {sys.argv[0]} <directory>")

    directory = sys.argv[1]
    if not os.path.exists(directory):
        error(f"'{directory}' does not exists")

    # wheels
    files = list(glob.glob(os.path.join(directory, "*.whl")))
    # sdist
    files += list(glob.glob(os.path.join(directory, "*.tar.gz")))

    output = HTML_START
    for file in files:
        file = os.path.basename(file)
        output += f'    <a href="{file}">{file}</a>\n'
    output += HTML_END

    print(output)
