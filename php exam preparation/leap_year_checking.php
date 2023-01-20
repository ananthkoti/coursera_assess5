<?php
 $n=readline("enter a year: ");
    if($n%4==0 && $n%400==0){ // condition to check entered year is a leap year or not
        echo "entered year is a leap year: ";
    }
    else{
        echo "it is not a leap year: ";
    }
?>