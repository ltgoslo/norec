# norec

This package provides a simple interface for working with the NoReC
dataset.

## Installation

To install dependencies:

```
$ pip install -r requirements.txt
```

To install norec:

```
$ pip install .
```

If you don't have root access, or don't want a system wide
installation, we recommend that you use
a [virtual environment](https://docs.python.org/3/tutorial/venv.html).

The package works with both Python 2 and 3, with data being read in as
unicode.

## Examples

Read html files and extract text:

```python
import norec

# Load set of html files and metadata from 'train'. `subset` can be
# one of 'train', 'dev' and 'test'. Load returns a generator yielding
# a tuple with the file contents and associated metadata.
train_data = norec.load("data/html.tar.gz", subset="train")

train_set = [(norec.html_to_text(html), metadata['rating'])
             for html, metadata in train_data]	

```


Read conllu and extract tokens:

```python
import norec

# Load set of conllu files and metadata from 'dev'.
train_data = norec.load("data/conllu.tar.gz", subset="dev")

# Extract tokens from conllu. conllu_to_tokens() returns a generator
# yielding an ordered dictionary of ConLL-U words. See
# https://github.com/EmilStenstrom/conllu for details on the format.
train_set = [([w['form'] for w in norec.conllu_to_tokens(conllu)],
              metadata['rating'])
             for conllu, metadata in train_data]
```
