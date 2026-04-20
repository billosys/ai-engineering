#!/bin/bash

HTML_FILE=$1
MD_FILE=$2

pandoc "$HTML_FILE" -f html -t gfm -o $MD_FILE --wrap=none
