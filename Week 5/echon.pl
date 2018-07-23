#!/usr/bin/perl -w



$rep= $ARGV[0];
$value= $ARGV[1];

$argLength= $#ARGV;


if ($argLength != 1){

	print STDERR "Usage: $0 <number of lines> <string>\n";

}

else {

	if ($rep =~ /^[0-9]/ ){
		
		for ($i=0 ; $i<$rep ; $i++){
		
			print "$value\n";

		}

	} 

	else {
		
		print STDERR "$0: argument 1 must be a non-negative integer\n";
	}

}
