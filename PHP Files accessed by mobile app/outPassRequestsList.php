<?php

$staff_name=$_GET['username'];
$con = mysql_connect("localhost","root","dhl1925702");
if (!$con)
{
 die('Could not connect: ' . mysql_error());
}
mysql_select_db("collegedb", $con);

$query = mysql_query("SELECT * FROM staff_login WHERE uname='".$staff_name."'");
$sql = mysql_fetch_array($query);
$staff_id=($sql['uid']);

$aflag = $sql['aflag'];

if($aflag == 1)
{
	$result = mysql_query("SELECT *FROM op_form WHERE A_id = '".$staff_id."' AND status = 0");
	while($row = mysql_fetch_assoc($result))
	{
		$output[] = $row;
	}
	print(json_encode($output));

}
else 
{
	$result1 = mysql_query("SELECT *FROM op_form WHERE H_id = '".$staff_id."' AND status = 1");
	while($row1 = mysql_fetch_assoc($result1))
        { 
                $output1[] = $row1;
        }
        print(json_encode($output1));

}

mysql_close($con);


?>
