#!/usr/bin/env perl
use strict;
use warnings;

my @args = @ARGV;

if (@args && $args[0] eq 'bookml/search_index.pl') {
  shift @args;
  exec 'python3', 'bookml-search-index.py', @args
    or die "cannot execute Python search indexer: $!";
}

exec $^X, @args or die "cannot execute Perl command: $!";
