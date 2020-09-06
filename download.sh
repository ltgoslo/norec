#!/bin/bash

NAME=norec
VERSION=1.0.1
ARCHIVE=$NAME-$VERSION.tar.gz
URL=https://www.mn.uio.no/ifi/english/research/projects/sant/data/norec/$ARCHIVE
DATA_DIR=data

echo "Downloading corpus from $URL..."
wget $URL

echo "Unpacking into $DATA_DIR..."
mkdir -p $DATA_DIR
tar xfz $ARCHIVE -C $DATA_DIR --strip-components=1

echo "Deleting $ARCHIVE..."
rm $ARCHIVE
