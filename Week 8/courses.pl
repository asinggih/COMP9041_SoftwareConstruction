#!/usr/bin/perl -w
#
#

$prefix = $ARGV[0];

$url = "http://www.timetable.unsw.edu.au/current/${prefix}KENS.html";

open $item, '-|', "wget -q -O- $url" or die;
while (<$item>) {
	print "$1\n"; #if />($prefix\d\d\d\d)</;
}

close $item;

print $url;


