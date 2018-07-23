#!/bin/sh


ITEMS=`ls | sort -d`

small="Small files: "
med="Medium files: "
lrg="Large files: "


for FILE in $ITEMS
do
	lineCount=`wc -l <$FILE`
	
	if [ $lineCount -lt 10  ]
	then
		small="$small$FILE "
	
	elif [ $lineCount -lt 100  ]
	then
		med="$med$FILE "

	else
		lrg="$lrg$FILE "
	
	fi

done

echo $small
echo $med
echo $lrg






