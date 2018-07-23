#!/bin/sh


#WTHH, why use spacess????
for item in *.jpg
do
	newname=`echo $item | sed "s/.jpg/.png/"`
 	
	if [ -f "$newname"  ]
	then
		echo "$newname already exists"
	
	else	
		convert "$item" "$newname" 
		rm "$item"
	fi


done


