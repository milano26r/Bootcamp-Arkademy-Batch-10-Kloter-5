<?php
/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

function betweenDays ($startDate, $endDate){
   $start    = new DateTime($startDate);
   $end      = (new DateTime($endDate))->modify('+1 day');
   $interval = new DateInterval('P1D');
   $period   = new DatePeriod($start, $interval, $end);
   foreach ($period as $dt) {
    echo "'" . $dt->format("Y-m-d") . "', ";
       
   } 
}

echo(betweenDays('2019-11-01', '2019-11-05' ));
