<?php  
$num = readline("enter a num to find factorial: ");  
$factorial = 1;  
for ($i=$num; $i>=1; $i--)   
{  
  $factorial = $factorial * $i;  
}  
echo "Factorial of $num is $factorial";  
?>  