# NoReC: The Norwegian Review Corpus
This repository distributes the Norwegian Review Corpus (NoReC), created for the purpose of training and evaluating models for document-level sentiment analysis. More than 35,000 full-text reviews (approx. 15 million tokens) have been collected from major Norwegian news sources and cover a range of different domains, including literature, movies, video games, restaurants, music and theater, in addition to product reviews across a range of categories. Each review is labeled with a manually assigned score of 1–6, as provided by the rating of the original author. 

# Sources and partners
NoReC was created as part of the SANT project (Sentiment Analysis for Norwegian Text), a collaboration between the Language Technology Group (LTG) at the Department of Informatics at the University of Oslo, the Norwegian Broadcasting Corporation (NRK), Schibsted Media Group and Aller Media. This first release of the corpus comprises 35,194 reviews extracted from eight different news sources: Dagbladet, VG, Aftenposten, Bergens Tidende, Fædrelandsvennen, Stavanger Aftenblad, DinSide.no and P3.no. In terms of publishing date the reviews mainly cover the time span 2003–2017, although it also includes a handful of reviews dating back as far as 1998.

# Terms of use
The data is distributed under a Creative Commons Attribution-NonCommercial licence (CC BY-NC 4.0), access the full license text here: https://creativecommons.org/licenses/by-nc/4.0/

The licence is motivated by the need to block the possibility of third parties redistributing the orignal reviews for commercial purposes. Note that **machine learned models**, extracted **lexicons**, **embeddings**, and similar resources that are created on the basis of NoReC are not considered to contain the original data and so **can be freely used also for commercial purposes** despite the non-commercial condition. 

# Formats and pre-processing
NoReC distributes two formats. The first is the CoNNL-U format, containing sentence segmented and tokenized text annotated with PoS tags and dependency graphs. This is considered the primary format. Secondly, we also distribute the canonical HTML representation of the `raw' review documents as described in

# Structure 
For each format (CoNLL-U / HTML), each review is stored as a separate file, with the filename given by the review ID. To facilitate a low
barrier of use for different types of end-users, we also include scripts for converting from CoNLL-U to running tokenized text (using either full-forms or lemmas) and from HTML to raw text without pre-processing. To facilitate replicability of experiments the corpus comes with pre-defined standard splits for training, development and testing, with a 80–10–10 ratio.

Metadata for each review is provided as a JSON object, all listed in a single file; `metadata.json`. 
