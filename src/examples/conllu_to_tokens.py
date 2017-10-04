import norec

# Load set of conllu files and metadata from 'dev'.
train_data = norec.load("data/conllu.tar.gz", subset="dev")

# Extract tokens from conllu. conllu_to_tokens() returns a generator
# yielding an ordered dictionary of ConLL-U words. See
# https://github.com/EmilStenstrom/conllu for details on the format.
train_set = [([w['form'] for w in norec.conllu_to_tokens(conllu)],
              metadata['rating'])
             for conllu, metadata in train_data]
