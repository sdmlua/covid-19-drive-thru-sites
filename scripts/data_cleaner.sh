#!/bin/sh

if [[ $(uname -s) == "Darwin" ]]
then
	# If using macOS, install gnu utils using homebrew
	echo $(python parse_datawrapper.py | grep -m1 "chartData:") | \
	awk 'NF' | gsed -e 's|\\||g;' | tr '\t' '|' | \
	ghead -n -1 | gsed 's|chartData: \"||'

else

	echo $(python parse_datawrapper.py | grep -m1 "chartData:") | \
	awk 'NF' | sed -e 's|\\||g;' | tr '\t' '|' | \
	head -n -1 | sed 's|chartData: \"||'
fi
	
