#!/usr/bin/perl -w
#
# 

foreach $arg (@ARGV) {

	if ($arg eq "--version") {
		print "$0: version 0.1\n";
		exit 0;
	}
		
	else {
		push @files, $arg;
	}
}

$N=10;
@biglist=();

if ($files[0] =~ /^[+-]?\d+$/) {
	my $temp =(shift @files)*-1;
	die "Usage: $0 -linenumbers filename\n" if $temp < 0;
	$N = $temp;
}



foreach $f (@files) {
    open $f, '<', $f or die "$0: Can't open $f: $!\n";
    
    if (scalar(@files) > 1){
    	print "==> $f <==\n";
    }
    
    while (my $line = <$f>) {
	push @biglist, $line;
    }
    
    close $f;
    
    my $limit=scalar(@biglist);
    my $startIdx= $limit-$N;


    if ($limit < 10) {
    	foreach $item (@biglist){
		print "$item";
	}
    }

    else {
    	for $idx ($startIdx .. $limit-1){
		print $biglist[$idx];
	}
    }

    @biglist=();

}


