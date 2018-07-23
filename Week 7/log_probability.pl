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

#print (scalar @arguments);
unless (scalar @arguments ==  1 ){
	die "No word to track\n";

}

@files = <lyrics/*.txt>;
$track = pop @arguments;
$track = lc $track;



my @filtered =();
my @total = ();

foreach $file (@files) {
	open $file, '<', $file or die "$0: Can't open $file: $!\n";
	#print "opening $file\n";
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
	$logProb = log(($occurence+1) / scalar @total);
	$totWords = scalar @total;
	#printf "%4d/%6d = %.9f %s\n", $occurence, $totWords, $probability, $file;
	printf "log((%d+1)/%6d) = %8.4f %s\n", $occurence, $totWords, $logProb, $file;
	@total=();
	@filtered=();
}

#return @out;



#@_= proc();
#print log(3/16359)






