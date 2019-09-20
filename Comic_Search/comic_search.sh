#!/bin/bash

# Title script
clear
echo "==========================================================="
echo "=             Marvel Comics Chronology Search             ="
echo "==========================================================="
echo "                       1975 - 2019                         " 
echo
echo "                  Enter keyword to search                  "
echo
echo "Ex: 'X-Men' will list all comics with 'X-Men' in the title."
echo "For multiple terms, separate titles with a '|'" 

# Search for term(s) including months; opens Vim with results; 
# adds blank line before each month for easier reading
read -p "-> " STERM

# if [ "$STERM" = "X-Men" ]; then
egrep -i -w "January|February|March|April|May|June|July|August|September|October|November|December|$STERM" Marvel_Complete_Chronology.txt | vim - -S "~/.vim/months.vim"

