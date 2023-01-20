<?php  
$num = readline("enter the number: "); 
// initially sum is zero 
$sum=0;  
// to traverse through the given number we use for loop
  for ($i =0; $i<=strlen($num);$i++)  
 {  
  $rem=$num%10;  //to access the last digit of the given number 
   $sum = $sum + $rem;  //storing remainder into sum
   $num=$num/10;  // update the input value
  }  
 echo "Sum of digits is $sum"; //print the sum 
 ?>  
 // reverse of a number and sum of digits is same but in reverse of a number we need to 