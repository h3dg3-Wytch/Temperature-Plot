#!/usr/bin/awk -f
#This awk script reads in the python temperature from a lab. The temps are
# in the second column
BEGIN  { positiveSum = 0
negativeSum = 0 } 

{result = $1 - 50
 
 if(result < 0)
   negativeSum = negativeSum + result
 else
   positiveSum = positiveSum + result

}



END {print negativeSum
print positiveSum }
