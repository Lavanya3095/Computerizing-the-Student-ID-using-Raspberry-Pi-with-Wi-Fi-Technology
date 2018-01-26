<?php
//$regno=$_POST['regno'];
$regno=$_POST['regno'];
//echo $regno;
$con = mysql_connect("localhost","root","dhl1925702");
//echo $date.$code.$regno;
if (!$con)
{
 die('Could not connect: ' . mysql_error());
}
mysql_select_db("collegedb", $con);
$result=mysql_query("SELECT * FROM attendance_student WHERE regno = '".$regno."'");
$row=mysql_fetch_assoc($result);
//print(json_encode($row));
$tot_hrs=$row['tot_hrs'];
$no_hrs=$row['no_hrs'];
$perc=($no_hrs/$tot_hrs)*100;
//$percentage=$perc*100;
//echo $row['tot_hrs'];
//echo $row['no_hrs'];
echo $perc;
//echo $percentage;
mysql_close(con);
?>
