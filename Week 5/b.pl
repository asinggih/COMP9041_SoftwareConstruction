#!/usr/bin/perl -w

# This below is like dict in py
#$a{"Hello how are you"}= 42;
#print $a{"Hello how are you"}, "\n";

while ($line = <STDIN>){
	chomp $line;
	if ($previous_line{$line}){
		print "SNap!!\n";
	
	}
	$previous_line{$line} = 42;
}







