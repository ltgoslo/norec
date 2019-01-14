# Copyright 2017 Eivind Alexander Bergem <eivinabe@ifi.uio.no>
# This file is part of norec.

# norec is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# norec is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with norec.  If not, see <http://www.gnu.org/licenses/>.

import json
import os.path
import lxml.html
from .conllu import parse_conllu

from .misc import TarFile

def load_metadata(filename):
    """Read json from file and return json object."""

    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)

def get_split_and_id(filename):
    """Extract split name and file id from filename."""

    head, tail = os.path.split(filename)

    return os.path.basename(head), os.path.splitext(tail)[0]

def load(filename, subset=None):
    """Load subset from NoReC file."""

    # Load metadata
    metadata = load_metadata(os.path.join(os.path.dirname(filename),
                                          "metadata.json"))

    # Open archive and iterate over files
    with TarFile.open(filename, "r|gz") as archive:
        for member_filename, fd in archive.get_files(encoding="utf-8"):
            split, ident = get_split_and_id(member_filename)

            # Only load files for specified subset
            if subset and split != subset:
                continue

            # Read file and yield contents and associated metadata
            yield fd.read(), metadata[ident]

def html_to_text(html):
    """Convert html to text, stripping all tags and removing content
enclosed in remove-tag."""

    return "\n\n".join(elem.text_content() for elem
                       in lxml.html.fragments_fromstring(html)
                       if elem.tag != "remove")


def conllu_to_tokens(conllu):
    """Extract tokens from ConLL-U."""

    for sentence in parse_conllu(conllu):
        for word in sentence:
            yield word
