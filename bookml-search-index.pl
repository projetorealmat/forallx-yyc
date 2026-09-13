#!/usr/bin/env perl
use warnings;
use strict;
use File::Find;
use JSON::XS;
use XML::LibXML;

use lib 'bookml';
use bookml;

print STDERR "REALMat search indexer\n";

my @files;
my @index;

die 'must specify a folder' unless scalar @ARGV == 1;

File::Find::find(
  {
    preprocess => sub { sort @_; },
    wanted     => sub {
      push(@files, bookml::decode_fs($_)) if (-f $_ && m/\.html$/i);
    }
  },
  bookml::encode_fs($ARGV[0])
);

my $parser = XML::LibXML->new(
  {
    suppress_errors   => 1,
    suppress_warnings => 1,
    recover            => 2
  }
);

sub text_content {
  my ($node) = @_;
  my $text = '';

  for my $child ($node->childNodes) {
    my $type = $child->nodeType;

    if ($type == 3 || $type == 4) {
      $text .= ' ' . $child->nodeValue;
      next;
    }

    next unless $type == 1;

    my $name = lc($child->nodeName);
    next if $name eq 'annotation'
      || $name eq 'nav'
      || $name eq 'script'
      || $name eq 'style';

    if ($child->hasAttribute('alt')) {
      $text .= ' ' . $child->getAttribute('alt') . ' ';
    } elsif ($child->hasAttribute('alttext')) {
      $text .= ' ' . $child->getAttribute('alttext') . ' ';
    } elsif ($child->hasAttribute('aria-label')) {
      $text .= ' ' . $child->getAttribute('aria-label') . ' ';
    } else {
      $text .= text_content($child);
    }
  }

  $text =~ s/\s+/ /g;
  $text =~ s/^\s+|\s+$//g;
  return $text;
}

for my $file (@files) {
  my $doc = $parser->load_html(location => bookml::encode_fs($file));
  my @titles = $doc->findnodes('//title/text()');
  my $title = @titles ? $titles[0]->string_value : '';

  my @urls = reverse(
    map { $_->string_value }
      $doc->findnodes('//link[contains("up up up up up up up up up",@rel)]/@href')
  );
  push(@urls, $file);

  my @bodies = $doc->findnodes('//body');
  my $text = @bodies ? text_content($bodies[0]) : '';

  push(@index, [\@urls, $title, $text]);
}

bookml::open_file(my $fh, '>', 'search_index.json')
  or die "cannot write search_index.json: $!";
print $fh encode_json(\@index);
