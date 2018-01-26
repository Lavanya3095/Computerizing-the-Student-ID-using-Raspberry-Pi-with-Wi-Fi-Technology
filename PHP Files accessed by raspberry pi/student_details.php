<?php

$name=$_POST['name'];
$reg=$_POST['regno'];
$con = mysql_connect("localhost","root","dhl1925702");

if (!$con)
 {
 die('Could not connect: ' . mysql_error());
 }
mysql_select_db("collegedb", $con);

$result = mysql_query("SELECT *FROM student_details WHERE Sname = '".$name."' AND Sregno = '".$regno."'");
//echo "<table>";
$row = mysql_fetch_array($result);
//print ($row['Sfname']);

while($row = mysql_fetch_assoc($result))
 {
       echo "<tr><td>".$row['name']."</td><td>".$row['regno']."</td><tr>";
       $output[]=$row;
 }

print(json_encode($output));

//echo "</table>";

mysql_close($con);


?>

