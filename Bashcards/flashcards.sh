#!/bin/bash
# https://www.youtube.com/watch?v=lX8jqo70r1I
# Script via Connor McDaniel

set -e

# Configuration 
FILE="$HOME/Scripts/flashcards.csv"

main() { 
	IFS=$'\t'; read -a q <<<$(shuf -n 1 "$FILE") 
	echo "======================================================"
	echo "Category: ${q[0]}"
	echo "Question: ${q[1]}"
	read _
	echo "Answer: ${q[2]}"
	echo ''
}

while true; do
	main
done
