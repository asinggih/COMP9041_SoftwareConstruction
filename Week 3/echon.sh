#!/bin/sh

usage () {	
  echo "Usage: $0 <number of lines> <string>"
}

error () {
  echo "$0 argument 1 must be a non-negative integer"
}


REPEAT=$1
ITEM=$2

re='^[0-9]'

if ! [[ $REPEAT =~ $re ]];
then
	error

else	
	if [ $REPEAT -gt 0 ];
	then

		for (( i=0 ; i<$REPEAT ;i++ ))
		do
			echo "$ITEM"
		done
	
	else
		error
	fi

fi




