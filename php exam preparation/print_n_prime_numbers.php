<?php
$n=readline("enter the number to find primes upto that number: ");
    for($i = 1; $i <= $n; $i++)
      $count = 0;
      for($j = 2; $j <= $i/2; $j++) {
        //only not prime numbers
                if ($i % $j == 0) {
                  $count++;
                  break;
                }
      }
      if ($count == 0) {
                echo"$i is prime number<br/>";
      }
    
  ?>