<?php  
$num = readline("enter a num: ");  
$revnum = 0;  
while ($num > 1)  
{  
$rem = $num % 10;  //to get last digit of the given number
$revnum = ($revnum * 10) + $rem; //storing the remaider number with reverse number 
$num = ($num / 10); //  update the given input
}  
echo "Reverse of a number is: $revnum";  
?>  