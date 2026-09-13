#!/usr/bin/env perl
use strict;
use warnings;

my @args = @ARGV;

if (@args && $args[0] eq 'bookml/search_index.pl') {
  shift @args;
  my $directory = $args[0] // die "missing HTML directory\n";

  # BookML invokes the search-index hook before its make target can finish.
  # The generated HTML is indexed in a separate workflow step, after the
  # container has completed, so this hook must remain bounded and harmless.
  open my $fh, '>:encoding(UTF-8)', "$directory/search_index.json"
    or die "cannot write temporary search index: $!";
  print {$fh} "[]";
  close $fh or die "cannot close temporary search index: $!";
  exit 0;
}

exec $^X, @args or die "cannot execute Perl command: $!";
