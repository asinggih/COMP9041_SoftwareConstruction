#!/usr/bin/perl -w


$line = <STDIN>;

$newVar = "";

$re='^[0-9]';


foreach $item (split //, $line){
	
	if ($item =~ $re){

		if ($item < 5){
			$newVar .="<";
		}

		elsif ($item > 5){
			$newVar .=">";
		}

		else{
			$newVar .="$item";	
		}
	
	}
	else{
		$newVar .="$item";	
	}
}

print "$newVar";


