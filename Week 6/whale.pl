#!/usr/bin/perl -w
##
#


$flag = 1;
$track = $ARGV[0];


while ( $line = <STDIN> ){

	($value) = $line=~ /(\d+)/;
	($key) = $line=~ /(\D+)/;
	$key =~ s/^\s+|\s+$//g; 	# trimming leading or trailing spaces
	$key =~ s/ +/ /g;		# trim spaces in the middle of the string
	$key = lc $key;
	$key =~ s/s$//;
	

	if (exists $whaleHoA{$key}) {
	
		$whaleHoA{"$key"}[0] += $value+0;			  
		$whaleHoA{"$key"}[1] += 1;
	}

	else {
		
		$whaleHoA{"$key"} = [ $value ];
		push @{ $whaleHoA{"$key"} }, 1;
	
	}	

}

#print $#ARGV;

if ($flag == 1) {
	printf("%s observations: %d pods, %d individuals\n", "$track", "$whaleHoA{$track}[1]", "$whaleHoA{$track}[0]");

}

#else {
# 
#}
	
