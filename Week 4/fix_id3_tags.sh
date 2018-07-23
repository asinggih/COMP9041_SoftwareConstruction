#!/bin/sh



folder=$1

for music in $folder*/*.mp3
do
	biglist=`echo $music | egrep -o '/.*[0-9]{4}.*' | cut  -c2-`
	albumName=`echo $biglist | cut -d',' -f1`
	albumYear=`echo $biglist | egrep -o '[0-9]{4}/' | sed "s_/__"`
	songName=`echo $biglist | cut -d'-' -f2 | cut -d' ' -f2-`
	track=`echo $biglist | egrep -o '/[0-9]+' | sed "s_/__"`
	artist=`echo $biglist | cut -d'-' -f3 | cut -d' ' -f2-  | sed "s_.mp3__"`
	

	#echo 'end'
 	#echo "$music"
	#echo $songName
	id3tag -a"$artist" "$music"	
	id3tag -A"$albumName" "$music"	
	id3tag -y"$albumYear" "$music"
	id3tag -s"$songName" "$music"
	id3tag -t"$track" "$music"
done


