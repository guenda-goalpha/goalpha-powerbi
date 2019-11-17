<?php
//$servername = "localhost";
//$username = "root";
//$password = "";
//$dbname = "datas";

$servername = "35.240.25.3";
$username = "postgres";
$password = "imbEvent2019";
$dbname = "goalpha";

$connStr = "host=35.240.25.3 port=5432 dbname=goalpha user=postgres password=imbEvent2019";
$conn = pg_connect($connStr);

if (@$conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


if (isset($_POST['endpoint']) && isset($_POST['query']))
{
    $endpoint = $_POST['endpoint'];
    $query = $_POST['query'];

    //Heqim whitespaces of the string
    $endpoint = trim($endpoint);
    $query = trim($query);

    //replace space with underscore
    $endpoint = str_replace(" ","_",$endpoint);

    $sql = "INSERT INTO datas (end_point, query) VALUES ('".$endpoint."','".$query."')";
    if (pg_query($conn,$sql)) {
        echo "Te dhenat u shtuan!";
        $new_url = "http://b8dca45a.ngrok.io/api/".$endpoint;
        header("Location: ".$new_url);
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}


?>