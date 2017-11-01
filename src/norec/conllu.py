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

CONLLU_FIELDS = ('id', 'form', 'lemma', 'upostag', 'xpostag', 'feats',
                'head', 'deprel', 'deps', 'misc')

def parse_conllu_line(line):
    """Parse CoNLL-U line and return dictionary."""

    # Created dictionary and do type conversion
    return dict(zip(CONLLU_FIELDS, line.split("\t")))

def empty_line(line):
    """Check if line is emtpy."""

    return not bool(line.strip())

def is_comment(line):
    """Check if line is comment."""

    return line.startswith("#")

def parse_conllu(conllu):
    """Parse ConLL-U file and return generator over sentences."""

    sentence = []

    for line in conllu.split("\n"):
        # Ignore comments
        if is_comment(line):
            continue

        # Emtpy line, marks end of sentence
        if empty_line(line):
            yield sentence
            sentence = []
            continue

        # Parse line
        w = parse_conllu_line(line)

        if w:
            sentence.append(w)

    if sentence:
        yield sentence
