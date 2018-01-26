<?php
$servername = "localhost";
$username = "root";
$password = "dhl1925702";
$dbname = "collegedb";
$pname = $_POST['name'];
$pregno = $_POST['regno'];
$pdate = $_POST['date'];
$pevent =$_POST['reason'];
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn)
{
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
                $query = "INSERT INTO od_form (table_name, name, regno, date, reason, status, A_id, H_id) VALUES ('ON-DUTY','".$pname."','".$pregno."','".$pdate."','".$pevent."',0,'".$paid."','".$phid."')";
                mysqli_query($conn, $query);
                echo "on-duty applied";
        }
    }
} else
{
    echo "0 results";
}
mysqli_close($conn);
?> 
