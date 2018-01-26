<?php

$date=$_POST['date'];
$code=$_POST['code'];
$regno=$_POST['regno'];
echo $date;
$con = mysql_connect("localhost","root","dhl1925702");
//echo $date.$code.$regno;
if (!$con)
{
 die('Could not connect: ' . mysql_error());
}
mysql_select_db("collegedb", $con);

$result=mysql_query("SELECT * FROM student_details WHERE Sregno = '".$regno."'");
$row = mysql_fetch_assoc($result);
$auname= $row['Aid'];

$result1 = mysql_query("SELECT *FROM attendance_staff WHERE uid = '".$auname."'");
$row1 = mysql_fetch_assoc($result1);
$staff_code=$row1['code'];
$staff_date=$row1['date'];
$staff_hour = $row1['hour'];
//echo $staff_date;
//echo "Staff is marking for ".$staff_hour;
if(!strcmp($code,$staff_code) && (!strcmp($date,$staff_date)))
{
	//echo $staff_date;
	if($staff_hour==1)
	{
		$result2=mysql_query("UPDATE attendance_student SET hour1='P' WHERE regno = '".$regno."'");
		echo "Marked present for hour 1";
		$get=mysql_query("SELECT * FROM attendance_student WHERE regno='".$regno."'");
		$get1 = mysql_fetch_assoc($get);
		$temp_no_hrs= $get1['no_hrs'];
		$a_no_hrs=2;
		$temp_no_hrs=$get1['no_hrs']+$a_no_hrs;
		$result3=mysql_query("UPDATE attendance_student SET no_hrs='".$temp_no_hrs."' WHERE regno = '".$regno."'");
	}
	if($staff_hour==2)
        {
                 $result2=mysql_query("UPDATE attendance_student SET hour2='P' WHERE regno = '".$regno."'");
		 echo "Marked present for hour 2";
		 $get=mysql_query("SELECT * FROM attendance_student WHERE regno='".$regno."'");
                 $get1 = mysql_fetch_assoc($get);
                 $temp_no_hrs= $get1['no_hrs'];
		 $a_no_hrs=3;
		 $temp_no_hrs=$get1['no_hrs']+$a_no_hrs;
                 $result3=mysql_query("UPDATE attendance_student SET no_hrs='".$temp_no_hrs."' WHERE regno = '".$regno."'");
        }
	if($staff_hour==3)
        {
                $result2=mysql_query("UPDATE attendance_student SET hour3='P' WHERE regno = '".$regno."'");
		echo "Marked present for hour 3";
		$get=mysql_query("SELECT * FROM attendance_student WHERE regno='".$regno."'");
                $get1 = mysql_fetch_assoc($get);
                $temp_no_hrs= $get1['no_hrs'];
		$a_no_hrs=3;
		$temp_no_hrs=$get1['no_hrs']+$a_no_hrs;
                $result3=mysql_query("UPDATE attendance_student SET no_hrs='".$temp_no_hrs."' WHERE regno = '".$regno."'"); 
	}

}
else
{
	echo "Attendance not recorded";
}

mysql_close($con);
?>
