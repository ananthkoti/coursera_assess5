<?php
function primeCheck($number){
    if ($number == 1)
    return 0;
    for ($i = 2; $i<= $number/2; $i++){//prime num starts from 2
        if ($number % $i == 0)//checks wheather given num is divissible by 2 or not
            return 0;//it is not a prime sincce divisible by 2 also along with 1 and itself
    }
    return 1;
}
 
$number = readline("enter a number to check wheather it is prime or not: ");
$flag = primeCheck($number);
if ($flag == 1)
    echo "Prime";
else
    echo "Not Prime"
?>