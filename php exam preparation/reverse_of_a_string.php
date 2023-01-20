<?php  
$string = readline("enter the string to reverse: ");  
$length = strlen($string);  
for ($i=($length-1) ; $i >= 0 ; $i--)   
{  
  echo $string[$i];  
}  
?>  