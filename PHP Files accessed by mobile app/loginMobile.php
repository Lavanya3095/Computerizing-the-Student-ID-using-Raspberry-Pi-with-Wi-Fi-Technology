<?php
        $name = $_POST["username"];
        $pwd = $_POST["pwd"];
        $con = mysql_connect("localhost","root","dhl1925702");
        if (!$con)
        {
        die('Could not connect: ' . mysql_error());
        }
        mysql_select_db("collegedb", $con);
        $result = mysql_query("SELECT * FROM staff_login WHERE uname = '".$name."' AND  pwd = '".$pwd."'");
        $row = mysql_fetch_array($result);
       	if($row['uname'] == $name && $row['pwd'] == $pwd)
        {
		echo "success";
        }
        else
       	{
         	echo "failure";
        }
        mysql_close($con);
?>
