<?php
	$host= "localhost";
	$username= "root";
	$password= "";
	$dbname="tekete";

	$connection=mysqli_connect($host,$username,$password,$dbname) or die(" No connection to the database");
	$query=mysqli_query($connection,$dbname);
	/*($connection)
	{
		echo "Please Wait";
	}*/
?>