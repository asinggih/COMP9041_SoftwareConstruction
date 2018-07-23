#!/bin/sh

file=$1

egrep 'COMP[29]041' $file | cut -d',' -f2 | cut -d' ' -f2 | sort -d | uniq -c | sort -g | tail -n 1 | sed 's/[^\t]*[0-9] //'
