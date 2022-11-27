<?php

#Paket von apache php (Erzeugt connect obj)
$connect = mysqli_connect(
    'db', # service name
    'user', # username
    'test', # password
    'php_docker' # db table
);

$table_name = "php_docker_table";#Tabellen Name in Php-Admin 

#Ausgabe eines einzelnen Users aus der Tabelle
$ausgabeUser = "SELECT * FROM $table_name WHERE USR_ID=2";

$response = mysqli_query($connect, $ausgabeUser);

echo "<strong>$table_name: </strong>";
while($i = mysqli_fetch_assoc($response))
{
    echo "<p>".$i['USR_ID']."</p>";
    echo "<p>".$i['User']."</p>";
    echo "<p>".$i['Password']."</p>";
    echo "<hr>";
}

#Abfrage nach User und Passwort
$sql = "SELECT User, Password FROM $table_name WHERE User='" .
        $_POST["User"] . "' AND Password='" . $_POST["Password"] . "'";

$result = $connect->query($sql);
echo $sql;
echo "<br/>";
if($result != false)
    echo $connect->error;
while($result != false && $row = $result->fetch_assoc()){
    echo $row["User"] . " - " . $row["Password"];
}
$connect->close();
?>