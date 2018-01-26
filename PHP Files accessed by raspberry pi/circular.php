<?php
$pdate=$_POST['date'];
//$pdate="2017-03-18";
$con = mysql_connect("localhost","root","dhl1925702");
if (!$con)
 {
 die('Could not connect: ' . mysql_error());
 }
mysql_select_db("collegedb", $con);

$result = mysql_query("SELECT date,content FROM circular WHERE date = '".$pdate."'");
//echo "<table>";
while($row = mysql_fetch_assoc($result))
 {
      // echo "<tr><td>".$row['name']."</td><td>".$row['regno']."</td><tr>";
        $output[]=$row;
 }
if (mysql_num_rows($result) == 0) {
    echo "No circulars for today";
}
else{
print(json_encode($output));
}
//echo "</table>";

mysql_close($con);

?>

