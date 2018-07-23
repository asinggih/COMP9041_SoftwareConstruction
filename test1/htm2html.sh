#!/bin/sh





for i in *.htm
do
	#echo $i
	temp=`echo $i | sed 's/htm/html/'`
	
	if test -e "$temp"  
	then
		echo "$temp exists"
	else
		cp "$i" "$temp"
		rm "$i"
	fi
done
