#!/usr/bin/perl -w
#

@biglist = ();
while ( $line = <> ){
	
	push @biglist, ( $line=~ /([a-zA-Z]+)/g );
	
}
$out= scalar @biglist;
print "$out words\n"
