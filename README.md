# NoReC: The Norwegian Review Corpus
This repository distributes the Norwegian Review Corpus (NoReC), created for the purpose of training and evaluating models for document-level sentiment analysis. More than 43,000 full-text reviews have been collected from major Norwegian news sources and cover a range of different domains, including literature, movies, video games, restaurants, music and theater, in addition to product reviews across a range of categories. Each review is labeled with a manually assigned score of 1–6, as provided by the rating of the original author. The accompanying [paper](http://www.lrec-conf.org/proceedings/lrec2018/pdf/851.pdf) by Velldal et al. at LREC 2018 describes the (initial release of the) data in more detail. 

# Sources and partners
NoReC was created as part of the [SANT](https://www.mn.uio.no/ifi/english/research/projects/sant/) project (Sentiment Analysis for Norwegian Text), a collaboration between the Language Technology Group (LTG) at the Department of Informatics at the University of Oslo, the Norwegian Broadcasting Corporation (NRK), Schibsted Media Group and Aller Media. This _2nd release, v.2.1_ of the corpus comprises 43,436 review texts extracted from eight different news sources: Dagbladet, VG, Aftenposten, Bergens Tidende, Fædrelandsvennen, Stavanger Aftenblad, DinSide.no and P3.no. In terms of publishing date the reviews mainly cover the time span 2003–2019, although it also includes a handful of reviews dating back as far as 1998.

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

If you publish work that uses or references the data, please cite our [LREC article](http://www.lrec-conf.org/proceedings/lrec2018/pdf/851.pdf). BibEntry: 

```
@InProceedings{VelOvrBer18,
  author = {Erik Velldal and Lilja {\O}vrelid and 
            Eivind Alexander Bergem and  Cathrine Stadsnes and 
            Samia Touileb and Fredrik J{\o}rgensen},
  title = {{NoReC}: The {N}orwegian {R}eview {C}orpus},
  booktitle = {Proceedings of the 11th edition of the 
               Language Resources and Evaluation Conference},
  year = {2018},
  address = {Miyazaki, Japan},
  pages = {4186--4191}
}
```
# Some statistics

## Distribution over year and publication source
All splits combined

|   year |   ap |   bt |   db        |   dinside |   fvn |   p3 |   sa |   vg |   Total |
|-------:|-----:|-----:|------------:|----------:|------:|-----:|-----:|-----:|--------:|
|  2003* |    0 |    4 |           0 |       143 |     0 |   25 |    0 |  286 |     458 |
|   2004 |    0 |   44 |           0 |       142 |     0 |   12 |   19 |  984 |    1201 |
|   2005 |    0 |    0 |           0 |       179 |     0 |    6 |  224 |  909 |    1318 |
|   2006 |    0 |    0 |           0 |       240 |     0 |   11 |  294 |  778 |    1323 |
|   2007 |    0 |    0 |           0 |       139 |     0 |  127 |  400 |  725 |    1391 |
|   2008 |    0 |    0 |           0 |       119 |     0 |  216 |  369 |  739 |    1443 |
|   2009 |    0 |   52 |         377 |       163 |    27 |  428 |  259 |  815 |    2121 |
|   2010 |    0 |  100 |         642 |       260 |   156 |  571 |  309 |  769 |    2807 |
|   2011 |    1 |   51 |         592 |       284 |   146 |  652 |  362 |  900 |    2988 |
|   2012 |    2 |  150 |         613 |       257 |   332 |  611 |  561 |  763 |    3289 |
|   2013 |    4 |  160 |         527 |       216 |   213 |  619 |  433 | 1058 |    3230 |
|   2014 |   39 |  291 |         501 |       236 |   357 |  546 |  387 | 1191 |    3548 |
|   2015 |  249 |  235 |         728 |       245 |   456 |  499 |  620 |  849 |    3881 |
|   2016 |  309 |  340 |         809 |       177 |   321 |  439 |  682 |  715 |    3792 |
|   2017 |  649 |  491 |         921 |       248 |   692 |  567 |  822 |  687 |    5077 |
|   2018 |  605 |  470 |         885 |       194 |   466 |  339 |  860 |  492 |    4311 |
|   2019 |  260 |  167 |          95 |        30 |   160 |   36 |  346 |  165 |    1259 |

`2003*`: Including the 31 documents 1998-2002

## Distribution over split and rating 

| split   |   1 |    2 |    3 |     4 |     5 |    6 |   Total |
|:--------|----:|-----:|-----:|------:|------:|-----:|--------:|
| dev     |  51 |  225 |  707 |  1409 |  1678 |  278 |    4348 |
| test    |  27 |  242 |  706 |  1385 |  1714 |  266 |    4340 |
| train   | 379 | 2287 | 6004 | 11304 | 12614 | 2161 |   34749 |

## Distribution over split and category
| split   |   games |   literature |   misc |   music |   products |   restaurants |   screen |   sports |   stage |   Total |
|:--------|--------:|-------------:|-------:|--------:|-----------:|--------------:|---------:|---------:|--------:|--------:|
| dev     |     179 |          539 |     28 |    1445 |        347 |            94 |     1569 |       15 |     132 |    4348 |
| test    |     180 |          547 |     24 |    1444 |        345 |            98 |     1579 |       16 |     107 |    4340 |
| train   |    1453 |         4337 |    156 |   11777 |       2771 |           745 |    12536 |      118 |     856 |   34749 |

## What's new

**Version 2.1 November 2023:**   
We have cleaned NoReC, introducing the following changes:

### Updated "category" data
There were previously 4619 texts in the "misc" category. We have assigned the correct category for most these, based on the source categories, source tags and manual inspection. The remaining 208 texts labeled "misc" should now be truly miscellaneous, like reviews of podcasts, art exhibitions and politicians taking part in debates. 

We consider the "category" tag to be the best representation of _domain_ for the reviewed entity or event.
### Removed duplicates
177 reviews were found to be duplicates, cross-postings in more than one news outlet in the same media group. This reduced the toal count of reviews from 43614 to 43437. 