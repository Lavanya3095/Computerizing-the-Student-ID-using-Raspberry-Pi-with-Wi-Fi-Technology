<?php
$servername = "localhost";
$username = "root";
$password = "dhl1925702";
$dbname = "collegedb";
$pname = $_POST['name'];
$pregno = $_POST['regno'];
$preason = $_POST['reason'];
$pltime =$_POST['ltime'];
$prtime = $_POST['rtime'];
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT Sregno, Aid, Hid FROM student_details";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result))
    {

        if($row["Sregno"]==$_POST['regno'])
        {
                $paid = $row["Aid"];
                $phid = $row["Hid"];
		$query = "INSERT INTO op_form (name, regno, reason, l_time, r_time, status, A_id, H_id) VALUES ('".$pname."','".$pregno."','".$preason."','".$pltime."','".$prtime."',0,'".$paid."','".$phid."')";
		mysqli_query($conn, $query);
                echo "out pass applied";
        }
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?> 

