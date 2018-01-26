<?php

$staff_name=$_GET['username'];
$regno = $_GET['regno'];
$date = $_GET['date'];
$reason = $_GET['reason'];
$status_grant = $_GET['status'];
/*echo $staff_name.$regno.$date.$reason.$status_grant;
echo "hello";
$staff_name="adv_ece";
$date="2017-03-15";
$regno="31113104702";
$reason="fever";
$status_grant="granted";
echo strcmp($status_grant,"granted");*/

$con = mysql_connect("localhost","root","dhl1925702");

if (!$con)
{
 die('Could not connect: ' . mysql_error());
}
mysql_select_db("collegedb", $con);

$query = mysql_query("SELECT * FROM staff_login where uname='".$staff_name."'");
$sql = mysql_fetch_array($query);
$staff_id=($sql['uid']);
$aflag = $sql['aflag'];
//echo "Staff ID".$staff_id;
//$result = mysql_query("UPDATE leave_form SET status = 1 WHERE A_id= '".$staff_id."' AND regno = '".$regno."' AND date = '".$date."' AND reason = '".$reason."'");
if(!strcmp($status_grant,"granted"))
{
	if($aflag == 1)
	{
		$result1 = mysql_query("UPDATE od_form SET status = 1 WHERE A_id = '".$staff_id."' AND regno = '".$regno."' AND date = '".$date."' AND  reason = '".$reason."'");
		echo "Request has been granted";
	}
	else 
        { 
                $result2 = mysql_query("UPDATE od_form SET status = 3 WHERE H_id = '".$staff_id."' AND regno = '".$regno."' AND date = '".$date."' AND reason = '".$reason."'");
                echo "Request has been granted";
        }

}
else 
{
        if($aflag == 1)
        { 
                $result3 = mysql_query("UPDATE od_form SET status = 2 WHERE A_id = '".$staff_id."' AND regno = '".$regno."' AND date = '".$date."' AND reason = '".$reason."'");
                echo "Request has been denied";
        }
        else 
        { 
                $result4 = mysql_query("UPDATE od_form SET status = 4 WHERE H_id = '".$staff_id."' AND regno = '".$regno."' AND date = '".$date."' AND reason = '".$reason."'");
                echo "Request has been denied";
        }

}


mysql_close($con);


?>
