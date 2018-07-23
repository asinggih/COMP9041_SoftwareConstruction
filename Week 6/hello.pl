#!/usr/bin/perl -w
# it grabs numbers at the end of the line



while ($line = <STDIN>){
	if ($line =~ /(-?\d+(\.\d+)?)\D*$/){
	
		print "$1\n";
	}

}
