#!/usr/bin/env perl
use strict;
use warnings;

my @args = @ARGV;

if (@args && $args[0] eq 'bookml/search_index.pl') {
  $args[0] = 'bookml-search-index.pl';
}

exec $^X, @args or die "cannot execute Perl command: $!";
