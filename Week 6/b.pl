#!/usr/bin/perl -w
#
#
#
#

while ($line = <>){

	$line =~ /^(w+)\|.*, (\S*)/ or die;
	$course = $1;
	$first_name = $2;
	
	print $course;
	print $first_name;

}


