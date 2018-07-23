#!/bin/sh


usage () {

  echo "Usage: $0 <course code> e.g., COMP or OPTM"

}

argLength=$#

if [ $argLength != 1  ]
then
	usage
	exit
fi

courseCode=$1
firstChar=`echo $courseCode|cut -c 1`


year=2017
base="http://www.handbook.unsw.edu.au/vbook$year/brCoursesByAtoZ.jsp?StudyLevel"
ugrd="$base=Undergraduate&descr=$firstChar"
pgrd="$base=Postgraduate&descr=$firstChar"

#echo $ugrd
#echo $pgrd

wget -q -O- "$ugrd" "$pgrd" | egrep -o "$courseCode[0-9]{4}.html.*" | sed "s_.html\">_ _" | 
sed "s_</.*__" |
sort |
uniq 





