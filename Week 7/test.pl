

sub blob {

	$sum = 0;

	foreach $i (@_){
	
		$sum += $i;
	}

	return $sum;

}
