# NoReC: The Norwegian Review Corpus
This repository distributes the Norwegian Review Corpus (NoReC), created for the purpose of training and evaluating models for document-level sentiment analysis. More than 35,000 full-text reviews (approx. 15 million tokens) have been collected from major Norwegian news sources and cover a range of different domains, including literature, movies, video games, restaurants, music and theater, in addition to product reviews across a range of categories. Each review is labeled with a manually assigned score of 1–6, as provided by the rating of the original author. 

# Sources and partners
NoReC was created as part of the SANT project (Sentiment Analysis for Norwegian Text), a collaboration between the Language Technology Group (LTG) at the Department of Informatics at the University of Oslo, the Norwegian Broadcasting Corporation (NRK), Schibsted Media Group and Aller Media. This first release of the corpus comprises 35,194 reviews extracted from eight different news sources: Dagbladet, VG, Aftenposten, Bergens Tidende, Fædrelandsvennen, Stavanger Aftenblad, DinSide.no and P3.no. In terms of publishing date the reviews mainly cover the time span 2003–2017, although it also includes a handful of reviews dating back as far as 1998.

# Terms of use
The data is distributed under a Creative Commons Attribution-NonCommercial licence (CC BY-NC 4.0), access the full license text here: https://creativecommons.org/licenses/by-nc/4.0/

The licence is motivated by the need to block the possibility of third parties redistributing the orignal reviews for commercial purposes. Note that **machine learned models**, extracted **lexicons**, **embeddings**, and similar resources that are created on the basis of NoReC are not considered to contain the original data and so **can be freely used also for commercial purposes** despite the non-commercial condition. 

# Formats and pre-processing
The reviews are distributed in two different formats. The first (and primary) format is [CoNNL-U](http://universaldependencies.org/format.html), containing sentence segmented and tokenized text annotated with PoS tags and dependency graphs using [UDPipe](https://ufal.mff.cuni.cz/udpipe). Secondly, we also distribute a canonical HTML representation of the `raw' review documents, with all content preserved (only relevant extracted text is included in CoNLL-U). 

Metadata for each review is provided as a JSON object, all listed in a single file, `metadata.json`, indexed on the document id. The JSON objects record properties like the numerical rating (an integer in the range 1–6), the thematic category or domain, the URL of the original document, and so on. It also records which of the two official varieties of Norwegian is used, as detected using [langid.py](https://github.com/saffsd/langid.py).   

# Structure 
For each format (CoNLL-U / HTML), each review is stored as a separate file, with the filename given by the review ID. To facilitate a low barrier of use for different types of end-users, we also include scripts for converting from CoNLL-U to running tokenized text (using either full-forms or lemmas) and from HTML to raw text without pre-processing. To facilitate replicability of experiments the corpus comes with pre-defined standard splits for training, development and testing, with a 80–10–10 ratio. The data directory of the distribution is structured as follows, where the `train`/`dev`/`test` directories holds the individual files (e.g. `000042.conllu`):

```
data
├── metadata.json
├── conllu.tar.gz
│   ├── train
│   ├── dev
│   └── test
└── html.tar.gz
    ├── train
    ├── dev
    └── test
```
# Obtaining the data
```
git clone https://github.com/ltgoslo/norec
cd norec
./download.sh
```
Running `download.sh` will download a tar.gz archive of approx. 235M, unpack it into a directory `norec/data/`, before finally removing the archive file.
