#!/usr/bin/perl -w
#

foreach $arg (@ARGV){

	if ($arg eq "--version"){
		print "$0: version 0.1\n";
		exit 0;
	}
	else {
		push @files, $arg;
	}

}

$file = pop @files;
$track = pop @files;
$track = lc $track;

my @filtered =();
open $file, '<', $file or die "$0: Can't open $file: $!\n";
while ( $line = <$file>  ){
	$line = lc $line;
	my @biglist = ( $line=~ /([a-zA-Z]+)/g );
	push @filtered, grep (/^$track$/, @biglist);
}

$occurence = scalar @filtered;
print "$track occured $occurence times\n";


