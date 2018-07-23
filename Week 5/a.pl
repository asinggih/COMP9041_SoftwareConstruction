#!/usr/bin/perl -w


open IN, '<', ARGV[0] or die "$ARGV[0]: $!";

@a = <IN>;
@a = reverse @a
open OUT, '>', $ARGV[0] or die;
print OUT @a;
close OUT;


