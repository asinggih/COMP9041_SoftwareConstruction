#!/usr/bin/perl -w
#


foreach $arg (@ARGV){

	if ($arg eq "--version"){
		print "$0: version 0.1\n";
		exit 0;
	}
	else {
		push @arguments, $arg;
	}

}

@files = <lyrics/*.txt>;
$track = pop @arguments;
$track = lc $track;

my @filtered =();
my @total = ();

foreach $file (@files) {
	open $file, '<', $file or die "$0: Can't open $file: $!\n";
	while ( $line = <$file>  ){
		$line = lc $line;
		my @biglist = ( $line=~ /([a-zA-Z]+)/g );
		push @total,  ( $line=~ /([a-zA-Z]+)/g );
		push @filtered, grep (/^$track$/, @biglist);
	}
	
	$occurence = scalar @filtered;
	$file =~ s/lyrics\///;
	$file =~ s/.txt//;
	$file =~ s/\_/ /g;
	$probability = $occurence / scalar @total;
	$totWords = scalar @total;
	printf "%4d/%6d = %.9f %s\n", $occurence, $totWords, $probability, $file;
	@total=();
	@filtered=();
}

