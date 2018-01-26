<?php
#$pname=$_POST['name'];
$pregno=$_POST['regno'];

$con = mysql_connect("localhost","root","dhl1925702");

if (!$con)
 {
 die('Could not connect: ' . mysql_error());
 }
mysql_select_db("collegedb", $con);

$result = mysql_query("SELECT Sname,Sregno,Sdept,Sbatch,Scont,Sfname,Sdob,Sbldgp,Scont,Saddr FROM student_details WHERE Sregno = '".$pregno."';");
if(result)
{

}
//echo "<table>";
while($row = mysql_fetch_assoc($result))
 {
      // echo "<tr><td>".$row['name']."</td><td>".$row['regno']."</td><tr>";
	$output[]=$row;
 }

print(json_encode($output));

//echo "</table>";

mysql_close($con);


?>
