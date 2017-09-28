#!/bin/bash

NAME=norec
VERSION=1.0.0
ARCHIVE=$NAME-$VERSION.tar.gz
URL=http://folk.uio.no/eivinabe/$ARCHIVE
DATA_DIR=data

echo "Downloading corpus from $URL..."
wget $URL

echo "Unpacking into $DATA_DIR..."
tar xfz $ARCHIVE --transform "s/$NAME/$DATA_DIR/"

echo "Deleting $ARCHIVE..."
rm $ARCHIVE
