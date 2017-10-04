import norec

# Load set of html files and metadata from 'train'. `subset` can be
# one of 'train', 'dev' and 'test'. Load returns a generator yielding
# a tuple with the file contents and associated metadata.
train_data = norec.load("data/html.tar.gz", subset="train")

# Convert html to text and put in a list together with rating
train_set = [(norec.html_to_text(html), metadata['rating'])
             for html, metadata in train_data]
