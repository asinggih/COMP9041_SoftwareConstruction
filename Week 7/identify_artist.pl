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

unless (scalar @arguments ==  1 ){
	die "No word to track\n";

}

@files = <lyrics/*.txt>;


$debug = 0;

foreach $item (@arguments) {
	if ($item eq '-d'){
		$debug = 1;
		next;
	}
	
	$track = $item;

}

$track = lc $track;

@filtered =();
@total = ();


foreach $file (@files) {

	$file =~ s/lyrics\///;
	$file =~ s/.txt//;
	$file =~ s/\_/ /g;
	$artist = $file;

	my %log_prob;
	open $file, '<', $file or die "$0: Can't open $file: $!\n";
	#print "opening $file\n";
	while ( $line = <$file>  ){
		$line = lc $line;
		my @biglist = ( $line=~ /([a-zA-Z]+)/g );
		push @total,  ( $line=~ /([a-zA-Z]+)/g );
		push @filtered, grep (/^$track$/, @biglist);
	}
	
	$occurence = scalar @filtered;
	$logProb = log(($occurence+1) / scalar @total);
	$totWords = scalar @total;
	
	printf "log((%d+1)/%6d) = %8.4f %s\n", $occurence, $totWords, $logProb, $artist; 
	
	@total=();
	@filtered=();
}
