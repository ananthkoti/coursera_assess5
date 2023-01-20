<?php
$n;
$i=0;
$j=1;
$s=0;
// n-> upto to  how many times we need to perform series,i and j initialize first two values, s value to store(like temp var) and shift values.
$n=readline("enter the number of series: "); //taking input from user to print the series upto required times
echo $i." ";// to print first value (0th position)
echo $j." ";// to print second value(1st position)      
for($k=2;$k<$n;$k++){                             //to make sum of the series from 3rd element i.e 2nd position(because assumed from 0th position)
    $s=$i+$j;                          // to add previous two values and to store in variable s.
    echo $s." ";                   // we need added output  since s stores sum
    $i=$j;                                        // to move to its succeding position
    $j=$s;   
}    
?>