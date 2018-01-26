<?php

$staff_name=$_GET['username'];
$date=$_GET['date'];
$hour=$_GET['hour'];
$code=$_GET['code'];
/*$staff_name = "adv_cse";
$date = "2017-03-15";
$hour = "2";
$code = "dhl";*/
$con = mysql_connect("localhost","root","dhl1925702");
if (!$con)
{
 die('Could not connect: ' . mysql_error());
}
mysql_select_db("collegedb", $con);

/*To determine the staff ID and aflag (adv if aflag is 1)
$query = mysql_query("SELECT * FROM staff_login WHERE uname='".$staff_name."'");
$sql = mysql_fetch_array($query);
$staff_id=($sql['uid']);
$aflag = $sql['aflag'];*/

$result = mysql_query("UPDATE attendance_staff SET code = NULL WHERE uname = '".$staff_name."' AND date = '".$date."' AND hour = '".$hour."'");

$testResult = mysql_query("SELECT * FROM attendance_staff WHERE uname = '".$staff_name."'");
$row = mysql_fetch_assoc($testResult);
$testCode = $row ['code'];
if(strcmp($code,$testCode)){
	echo "Attendance session completed";
}

mysql_close($con);

?>
