#!/usr/bin/awk -f
#This awk script reads in the python temperature from a lab. The temps are
# in the second column
BEGIN  { time = 0 } 

{print $2}


END { }
