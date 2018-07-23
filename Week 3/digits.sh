#!/bin/sh

read USERINPUT

# var=$( echo $USERINPUT | tr '[^A-z]' x)
# echo $var
VAR=5
NEWSTRING=""

LIMIT=${#USERINPUT}

for (( i=0 ; i<$LIMIT ; i++ ))
do
	ITEM=${USERINPUT:$i:1}  # It's printing the characters using the index, from the variable USERINPUT
	lsp=`ls -l`
	echo "$lsp"	
	if echo $ITEM | egrep -q '^[0-9]'; #only take the item that contains number
		then

		if test $ITEM -lt $VAR;
			then	
			ITEM=$( echo $ITEM | tr "$ITEM" "<")
			

		elif test $ITEM -gt $VAR;
			then
			ITEM=$( echo $ITEM | tr "$ITEM" ">")
			
		fi
			

	else
		ITEM=$ITEM

	fi

	# echo $ITEM
	NEWSTRING="$NEWSTRING$ITEM"

	# echo $ITEM

done

echo $NEWSTRING





# echo $NEWSTRING
# echo ${#NEWSTRING}
