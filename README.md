**NB**: this repo holds an expanded raw-text version of the NoReC corpus. This version contains 8425 additional reviews. The legacy version of NoReC version 1 can be found [here](https://github.com/erikve/norec).

# NoReC: The Norwegian Review Corpus
This repository distributes the Norwegian Review Corpus (NoReC), created for the purpose of training and evaluating models for document-level sentiment analysis. More than 43,000 full-text reviews have been collected from major Norwegian news sources and cover a range of different domains, including literature, movies, video games, restaurants, music and theater, in addition to product reviews across a range of categories. Each review is labeled with a manually assigned score of 1–6, as provided by the rating of the original author. 

# Sources and partners
NoReC was created as part of the SANT project (Sentiment Analysis for Norwegian Text), a collaboration between the Language Technology Group (LTG) at the Department of Informatics at the University of Oslo, the Norwegian Broadcasting Corporation (NRK), Schibsted Media Group and Aller Media. This second release of the corpus comprises 43,425 reviews extracted from eight different news sources: Dagbladet, VG, Aftenposten, Bergens Tidende, Fædrelandsvennen, Stavanger Aftenblad, DinSide.no and P3.no. In terms of publishing date the reviews mainly cover the time span 2003–2019, although it also includes a handful of reviews dating back as far as 1998.

# Terms of use
The data is distributed under a Creative Commons Attribution-NonCommercial licence (CC BY-NC 4.0), access the full license text here: https://creativecommons.org/licenses/by-nc/4.0/

The licence is motivated by the need to block the possibility of third parties redistributing the orignal reviews for commercial purposes. Note that **machine learned models**, extracted **lexicons**, **embeddings**, and similar resources that are created on the basis of NoReC are not considered to contain the original data and so **can be freely used also for commercial purposes** despite the non-commercial condition. 

# Formats and pre-processing
The reviews are distributed as *.txt* files, split into train, dev, and test sets. The files contain sentence and paragraph segmented texts, processed using [UDPipe](https://ufal.mff.cuni.cz/udpipe).

Metadata for each review is provided as a JSON object, all listed in a single file, `metadata.json`, indexed on the document id. The JSON objects record properties like the numerical rating (an integer in the range 1–6), the thematic category or domain, the URL of the original document, and so on. It also records which of the two official varieties of Norwegian is used, as detected using [langid.py](https://github.com/saffsd/langid.py).   

# Structure 
Each review is stored as a separate file, with the filename given by the review ID. To facilitate replicability of experiments the corpus comes with pre-defined standard splits for training, development and testing, with a 80–10–10 ratio. The data directory of the distribution is structured as follows, where the `train`/`dev`/`test` directories holds the individual files (e.g. `000042.txt`):

```
data
├── metadata.json
├── train
├── dev
├── test
```

# Obtaining the data
```
git clone https://github.com/ltgoslo/norec
```

# Citing

If you publish work that uses or references the data, please cite [our LREC article](http://www.lrec-conf.org/proceedings/lrec2018/pdf/851.pdf): 

```
NoReC: The Norwegian Review Corpus
Erik Velldal, Lilja Øvrelid, Eivind Alexander Bergem, Cathrine Stadsnes, Samia Touileb, Fredrik Jørgensen
2018
http://www.lrec-conf.org/proceedings/lrec2018/pdf/851.pdf
```
