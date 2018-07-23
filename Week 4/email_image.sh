#!/bin/sh

#NOT DONE YETT

argLength=$#

for arg in $*  #takes everything that is in the argument. just like *args in python
do
	image="$arg"
	read -p "Address this email containing $image to?  " toAddress
	read -p "Message to accompany this image? " comments
	echo "$image sent to $toAddress"
done

