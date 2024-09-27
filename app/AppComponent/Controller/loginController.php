<?php
	include_once('../connection.php');
	
    $email =$_POST['email'] ;
    $username =$_POST['username'] ;
// define variables to empty values  
$nameErr = $surnameErr = $cellNoErr = $emailErr = $companyNameErr = $password1Err = $password2Err = "";  
$name = $surname = $cellNo = $email = $companyName = $password = $password2 = ""; 
  
//Input fields validation  
if ($_SERVER["REQUEST_METHOD"] == "POST") {  
      
//String Validation  
    if (empty($_POST["name"])) {  
         $nameErr = "Name is required";  
    } else {  
        $name = input_data($_POST["name"]);  
            // check if name only contains letters and whitespace  
            if (!preg_match("/^[a-zA-Z ]*$/",$name)) {  
                $nameErr = "Only alphabets and white space are allowed";  
            }			
    }  
    if (empty($_POST["surname"])) {  
        $surnameErr = "Surname is required";  
    } else {  
        $surname = input_data($_POST["surname"]);  
            // check if name only contains letters and whitespace  
            if (!preg_match("/^[a-zA-Z ]*$/",$surname)) {  
                $surnameErr = "Only alphabets and white space are allowed";  
            }  
    }
    //Email Validation   
    if (empty($_POST["email"])) {  
            $emailErr = "Email is required";  
    } else {  
            $email = input_data($_POST["email"]);  
            // check that the e-mail address is well-formed  
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {  
                $emailErr = "Invalid email format";  
            }  
     }  
    
    //Number Validation  
    if (empty($_POST["cellNo"])) {  
            $cellNoErr = "Phone no is required";  
    } else {  
            $cellNo = input_data($_POST["cellNo"]);  
            // check if mobile no is well-formed  
            if (!preg_match ("/^[0-9]*$/", $cellNo) ) {  
            $cellNoErr = "Only numeric value is allowed.";  
            }  
        //check mobile no length should not be less and greator than 10  
        if (strlen ($cellNo) != 10) {  
            $cellNoErr = "Mobile no must contain 10 digits.";  
            }  
    }
    if (empty($_POST["companyName"])) {  
        $companyNameErr = "Company Name is required";  
    } else {  
        $companyName = input_data($_POST["companyName"]);  
		$companyName=strtoupper($companyName); 
    }
	if (empty($_POST["password1"])) {  
        $password1Err = "Password is required";
	}
		// Given password
		$password1 = $_POST['password1'];
		$ecrypass=md5($password1);
		
		// Validate password strength
		$uppercase = preg_match('@[A-Z]@', $password1);
		$lowercase = preg_match('@[a-z]@', $password1);
		$number = preg_match('@[0-9]@', $password1);
		$specialChars = preg_match('@[^\w]@', $password1);

	if(!$uppercase || !$lowercase || !$number || !$specialChars || strlen($password1) < 8)
		{
			$password1Err ='Password should be at least 8 characters in length. Should include at least upper case letter, lowercase case letter, a number, and special character.';
		}
	if (empty($_POST["password2"])) {  
        $password2Err = "Field empty, please Confirm the password";
	}
	// Given password
	$password2 = $_POST['password2'];
    $ecrypass2=md5($password2);
		if($password1 !== $password2)
		{
			$password2Err = 'Passwords do not match!';
		}
	
}



function input_data($data) {  
  $data = trim($data);  
  $data = stripslashes($data);  
  $data = htmlspecialchars($data);  
  return $data;  
} 

?> 
