<style>  
.error {color: #FF0001};

.sidebar{
     background: linear-gradient(to right ,#f4524d 0% ,#5543ca 100%);
}
.logo{
    width:100px;
    height:100px;
    margin-bottom:50px;
}
.title{
    font-weight:normal;
}
.new
{
    font-size:13px;
    
}
.mobile{
    display:none;
}
.topbr{
    display:none;
}
.h3{
    font-size:20px;
    color:#5543ca;
}

@media (min-width: 320px) and (max-width: 765px) {
  
  .sidebar{
      display:none;
  } 
  
  .incident{
     display:none;
  }
  .mobile{
      display:block;
      width:94%;
      margin:0 auto;

  }
    .title2{
     display:block;
     text-transform: uppercase;
	 text-align: left;
	 letter-spacing: 3px;
	 font-size: 20px;
	 line-height: 25px;
     padding-bottom: 15px;
      color: #5543ca;
	 background: linear-gradient(to right ,#f4524d 0% ,#5543ca 100%);
	 -webkit-background-clip: text;
	 -webkit-text-fill-color: transparent;
	 font-weight:400px;
	
}
.mobileForm{
    
    width:100%;
    margin:0 auto;
}

.mobileForm .input-text{
    width:100%;
    height:35px;
    margin-top:-1.8%;
}
.topbr{
    display:block;
}
.mobileForm .label{
    font-size:14px;
}
  
}
</style> 

<!-------------------------------------------------------- THIS IS PHP -------------------------------------->

<?php
	include_once('../connection.php');
	
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

<!-------------------------------------------------------- THIS IS HTML COMBINED WITH PHP -------------------------------------->

<!DOCTYPE html>
<html lang="en">
<head>

    <meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tekete Management System </title>
	
    <!-- Bootstrap-->
	<link href="../css/bootstrap-4.4.1.css" rel="stylesheet">
	
	<link href="../css/style.css" rel="stylesheet">
	
	
	<link rel="icon" href ="https://tekete.co.za/logo.png" type="image/icon type">
	
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"> 
	
	<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
</head>	

 <body>
             <div class="topbr">
               <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow " style="z-index:9999999999;height:70px;top:0;">
                  
                    <!-- 
                    <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3" onclick="openSide()" style="margin-left:-8%;margin-top:2%">
                        <i class="fa fa-bars" hi></i>
                    </button>
                    <button id="sidebarClose" class="btn btn-link d-md-none rounded-circle mr-3" onclick="openClose()" style="display:none;margin-left:-8%;margin-top:2%">
                        <i class="fa fa-close" hi></i>
                    </button>
       
                    --->
                    <div style="display:flex;width:100%">
                      <div style="width:50%;margin-left:-1%">
                        <img src="../logo.png" class="" style="width:30%;margin-top:25%;float:left" onclick="window.location.href='index.php'"> 
                      </div>
                      <div style="width:50%;float:right;margin-left:4%">
                          
                           <input class="submit_btn" type="submit" value="Login" onclick="window.location.href='../userLogin'" name="login" style="width:50%;float:right;background:#fff;color:#484848;border:1px solid #484848" >
                       </div>
                    </div>
                </nav>
        </div>
<section class="mobile">
	<h1 class="title2">Tekete Management System</h1>
	<div style="color:#686868;margin-bottom:6%"><p>Register a new account</p></div>

	<div class= "incident-form ">
	<div class="sidebar" >
		<div class="admin col-lg-11">
			<center>
			    <img src="../logo.png" class="logo" onclick="window.location.href='../'">
			</center>
<!-- New -->
				<div class="items">
					<a class="new" style="font-size:16px" onclick=""><i class="fa fa-user-circle" aria-hidden="true"></i>Register</a>
					<a class="new" style="font-size:16px" onclick="../userLogin"><i class="fa fa-user-circle" aria-hidden="true"></i>login</a>
				</div>
		</div>
	</div>
	
	
	<div class="content">
<form  id ="myForm" action ="" action="../Controller/loginController.php" name = "frm" method ="post" >
    <div class="mobileForm">
			<label class= "label" for="name">Name</label> <span class="error">*</span><br>
		    <input id="nameM" class="input-text" type= "text" name="name" value = "" placeholder="" onchange="mobilekName()"  style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error" id="error_nameM"><?php echo $nameErr; ?> </span><br>
			<label class= "label" for="phone">Surname</label><span class="error">*</span><br>
			<input id="surnameM" class="input-text" type= "text" name="surname" value = "" placeholder="" onchange="mobileSurname()" style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error errmobile"  id="error_SurnameM"><?php echo $surnameErr ?></span><br>
			<label class= "label" for="phone">Cellphone No</label><span class="error">*</span><br>
			<input id="phoneM" class="input-text" type= "text" name="cellNo"  value = "" placeholder="" onchange="mobilePhone()" style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error" id="error_PhoneM"><?php echo $cellNoErr ?></span><br>
			<label class= "label" for="email">Email</label><span class="error">*</span><br>
			<input id="emailM" class="input-text" type= "email" name="email" value = "" placeholder="" onchange="mobileEmail()" style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error" id="err_emailM"><?php echo $emailErr ?></span><br>
			<label class= "label" for="phone">Company Name</label><span class="error">*</span><br>
			<select id="CompNameM" class="input-text"  name="companyName" placeholder="Company Name" value = ""  onchange="mobileCompany()"style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error" id="error_companyM"><?php echo $companyNameErr ?></span><br>
			       <option></option>
				   
				   <?php
				      $sql="select * from company where c_type='Sub'";
					  $res=mysqli_query($connection,$sql);
					  
					  while($row=mysqli_fetch_assoc($res)){
						  ?>
						  <option value="<?php echo $row['company_id'] ?>"><?php echo $row['c_name'];?></option>
						  
						 <?php
					  }
				   
				   
				   ?>
			    </select>
			<label class= "label" for="password">Password</label><span class="error">*</span><br>
			<input id="pswdM" class="input-text" type= "password" name="password1" value = "" placeholder="" onchange="mobilePass()" style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error" id="errorPassM"><?php echo $password1Err ?></span><br>
			<label class= "label" for="email">Confirm Password</label><span class="error">*</span><br>
			<input id="conPswdM" class="input-text" type= "password" name="password2" value = "" placeholder="" onchange="mobilePassword()" style="background-color:#F0F0F0;border:1px;border-bottom:1.2px solid lightblue;font-size:14px;border-radius:0px "/><span class="error" id="errorPasswordM"><?php echo $password2Err ?></span><br>
         <div style="margin:0 auto;margin-top:-4%;display:flex">
              <input class="submit_btn" type="submit" value="Register" id="myButton" name="insert" style="width:50%;"></td>
               <input class="clear_btn" type="button" value="Clear" name="clear" style="width:50%;" onclick="clearMobile()">
         </div>
     </div>
</form>
</div>
</section>

<section class="incident">
	<h1 class="title">Tekete Management System</h1>
	<div class= "incident-form ">
	<div class="sidebar" >
		<div class="admin col-lg-11">
			<center>
			    <img src="../tekete.png" class="logo"  onclick="window.location.href='../'">
			</center>
<!-- New -->
				<div class="items">
					<a class="new" style="font-size:16px" onclick="window.location.href=''"><i class="fa fa-user-circle" aria-hidden="true"></i>Register</a>
					<a class="new" style="font-size:16px" onclick="window.location.href='../userLogin'"><i class="fa fa-user-circle" aria-hidden="true"></i>login</a>
				</div>
		</div>
	</div>
	
	
	<div class="content">
<form  id ="myForm" action ="" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" name = "frm" method ="post" >
	<table class="table">
		<tr> 
			<td><label class= "label" for="name">Name</label> </td>
			<td><input id="name" class="input-text" type= "text" name="name" value = "" placeholder="Name" onchange="checkName()"/><span class="error" id="error_name">* <?php echo $nameErr; ?> </span></td>			
		</tr>
		<tr>
			<td><label class= "label" for="phone">Surname</label></td>
			<td><input id="surnameErr" class="input-text" type= "text" name="surname" value = "" placeholder="Surname" onchange="checkSurname()"/><span class="error"  id="error_Surname">* <?php echo $surnameErr ?></span></td>
		</tr>
		<tr>
			<td><label class= "label" for="phone">Cellphone No</label></td>
			<td><input id="phone" class="input-text" type= "text" name="cellNo"  value = "" placeholder="Cellphone No" onchange="checkPhone()"/><span class="error" id="error_Phone">* <?php echo $cellNoErr ?></span></td>
		</tr>
		<tr>
			<td><label class= "label" for="email">Email</label></td>
			<td><input id="emailErr" class="input-text" type= "email" name="email" value = "" placeholder="Email" onchange="checkEmail()"/><span class="error" id="err_email">* <?php echo $emailErr ?></span></td>
		</tr>
		<tr>
			<td><label class= "label" for="phone">Company Name</label></td>
			<td><select id="CompNameErr" class="input-text"  name="companyName" placeholder="Company Name" value = ""  onchange="checkCompany()"/>
			       <option>Company Name</option>
				   
				   <?php
				      $sql="select * from company where c_type='Sub'";
					  $res=mysqli_query($connection,$sql);
					  
					  while($row=mysqli_fetch_assoc($res)){
						  ?>
						  <option value="<?php echo $row['company_id'] ?>"><?php echo $row['c_name'];?></option>
						  
						 <?php
					  }
				   
				   
				   ?>
			    </select>
			
			<span class="error" id="error_company">* <?php echo $companyNameErr ?></span>
			</td>
		</tr>
		<tr>
			<td><label class= "label" for="password">Password</label></td>
			<td><input id="pswd" class="input-text" type= "password" name="password1" value = "" placeholder="Password" onchange="checkPass()"/><span class="error" id="errorPass">* <?php echo $password1Err ?></span></td>
		</tr>
		<tr>
			<td> <label class= "label" for="email">Confirm Password</label></td>
			<td> <input id="conPswd" class="input-text" type= "password" name="password2" value = "" placeholder="Confirm password" onchange="checkPassword()"/><span class="error" id="errorPassword">*<?php echo $password2Err ?></span></td>
		</tr>
		<tr>
			<td><input class="submit_btn" type="submit" id="myButton" value="Register" name="insert"/></td>
			<td><input class="clear_btn" type="button" value="Clear"  name="clear" onclick="clearField()"></td>
		</tr>
	</table>
</form>
</div>
</section>

<!-------------------------------------------------------- THIS IS SWEET ALERT SCRIPT -------------------------------------->
<script>
function redirect(){
	swal({
	title: "Welcome to TEKETE",
	text:"Registration details are sent to your email...",
	icon: "success",
	button: true,
})
.then((redirect) => {
  if (redirect) {
	window.location.href = "../userLogin";
  } 
});
}

//Error warning 

function error(){
	swal({
	title: "Error",
	text: "Username or Password incorrect!!",
	icon: "warning",
	button: true,
	dangerMode: true,
});
}	



function clearField(){
	
	var fields =["name","surnameErr","phone","CompNameErr","emailErr","conPswd","pswd"]
	
	var i,l=fields.length;
	var fieldname;
	var isComplete=0;
	
	for(i=0;i<l;i++){
		fieldname=fields[i];
		
		if(document.forms["myForm"][fieldname].value===""){
			
		}
		else{
			isComplete=1;
		}
	}
	
	if(isComplete===1){
  swal({
      title: "Are you sure you want to clear?",
      text: "You will not be able to recover this!",
      icon: "warning",
      buttons: [
        'No, cancel it!',
        'Yes, I am sure!'
      ],
      dangerMode: true,
    }).then(function(isConfirm) {
      if (isConfirm) {
         document.getElementById('myForm').reset();
      } else {
        
      }
    })
}
	
}






</script>

<!-------------------------------------------------------- THIS IS PHP -------------------------------------->

<?php  	
    if(isset($_POST['insert']))
	{

        $fields=mysqli_query($connection,"SELECT *  FROM users WHERE email ='$email'");
		$rows=mysqli_num_rows($fields);
		if($rows>0){
			echo '<script>		swal({
                  title: "ERROR",
                  text:"User Already Registered",
                  icon: "warning",
	              button: true,
	              dangerMode: true,
              })
            .then((Register) => {
               if (Register) {

                   window.location.href = "../adminLogin";
    
               }
            });</script>';
						
			
		}
		else{
            
           
	    $compName =$_POST['companyName'];
	     $fields=mysqli_query($connection,"SELECT * FROM company WHERE company_id ='$compName'");
	     
	     
	     while($row=mysqli_fetch_assoc($fields))
	     {
	         $company1=$row['c_name'];
	     }
	    
        
	        if($nameErr == "" && $surnameErr == "" && $cellNoErr == "" && $emailErr == "" && $companyNameErr == "" && $password1Err == "" && $password2Err == "") 
		    {  
			    ini_set( 'display_errors', 1 );
			    error_reporting( E_ALL );
			    
			    $to = "$email";
			    $subject = "Registration Details";
			    $from = "support@tekete.co.za";
           
			    $headers  = 'MIME-Version: 1.0' . "\r\n";
                $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";
			    $headers .= 'From: '.$from."\r\n".
                            'Reply-To: '.$from."\r\n" .
                            'X-Mailer: PHP/' . phpversion();
			    
			    //$message = "You have successfully registered.\n";  
			    //$message .= "Registration Details\n";
                //$message .= "Name: $name \n";
                //$message .= "Surname: $surname \n";
                //$message .= "Phone Number: $cellNo \n";
                //$message .= "Email Address: $email \n";
                //$message .= "Company Name: $companyName \n";
                //$message .= "Password: $password1 \n";
                
                
                $message = '<html>';
                $message .= '<body><h1>Registration Details</h1>';
                $message .= '<table>';
                $message .= '<tr><th style="text-align:left">Name:</th><td>'.$name.'</td></tr>';
                $message .= '<tr><th style="text-align:left">Surname:</th><td>'.$surname.'</td></tr>';
                $message .= '<tr><th style="text-align:left">Phone Number:</th><td>'.$cellNo.'</td></tr>';
                $message .= '<tr><th style="text-align:left">Email Address:</th><td>'.$email.'</td></tr>';
                $message .= '<tr><th style="text-align:left">Company Name:</th><td>'. $company1.'</td></tr>';
                $message .= '<tr><th style="text-align:left">Password:</th><td>'.$password2.'</td></tr>';
                $message .= '</table></body></html>';
			    
			        
			    if(mail($to,$subject,$message, $headers)) 
			    {
			       //echo"<script> alert('Emai sent')</script>";
			    } 
			    else 
			    {
			       echo"<script> alert('Message was not sent.')</script>";
			    }
			   
			    $sql= "Insert into users (first_name,last_name,mobile,company_id,email,password) 
				VALUES('$name','$surname','$cellNo','$companyName','$email','$ecrypass')";
			    $query=mysqli_query($connection,$sql);
			    echo '<script>redirect();</script>';
					/*echo '<script>	
					wal({
                          title: "Welcome to tekete!",
						  text:"Registration details are sent to your email...",
                          icon: "success",
                          button: "OK",
                        })
                     .then((Register) => {
                      if (Register) {

                            window.location.href = "usertest.php";
    
                         }
                    });</script>';*/	
			    die();
		    }
		    else 
		    {  
			    echo '<script> swal({
                       title: "FAILED",
					   text:"You did not fill up the form correctly!",
                       icon: "danger",
	                   button: true,
	                   dangerMode: true,
                     })</script>	';
		    }
	    }
	
	}
	
?>
</div>
</body>
</html>


<!--------------------------------------------VALIDATING WITH JAVASCRIPT----------------------------------------------------------------->
<script >
/*-----------------------JAVASCRIPT FUNCTIONS FOR VALIDATING---------------------------------------*/


/*-----------------------checking if the form is in complete before redirect------------------------*/
function redirect(page_name){
	
	var fields =["name","surnameErr","phone","CompNameErr","emailErr","conPswd","pswd"]
	
	var i,l=fields.length;
	var fieldname;
	var isComplete=0;
	
	for(i=0;i<l;i++){
		fieldname=fields[i];
		
		if(document.forms["myForm"][fieldname].value===""){
			
		}
		else{
			isComplete=1;
		}
	}
	
	if(isComplete===1){
		  swal({
              title: "The Form is not complete are your sure you want to close this?",
              text: "You will not be able to recover this!",
              icon: "warning",
              buttons: [
                    'No, cancel it!',
                    'Yes, I am sure!'
                  ],
              dangerMode: true,
              }).then(function(isConfirm) {
              if (isConfirm) {
                 window.location.href = page_name;
              } else {
        
            }
          })
	
	}
	else{
		window.location.href = page_name;
		
	}
	
}




/*--------------------------------------VALIDATING ALL INPUT FIELDS---------------------------------------*/

//Return false if string only contains white spaces" "
function checkEmpty(str){
   return str.trim().length===0;
}

//validating name field
function   checkName(){
	  var str=document.getElementById('name').value;
	  if(checkEmpty(str)===false){
	      if(!/[^A-Za-z ]/.test(str)&&str!=""){
               document.getElementById('error_name').innerHTML="";
	       }	
          else{
               document.getElementById('error_name').innerHTML="* Only alphabets and white space are allowed";  
           }	
	     }
 		 else{
			document.getElementById('error_name').innerHTML="* Only alphabets are allowed";   
		 }	
   		 
}



//Checking if surname is correct
function   checkSurname(){
	  var str=document.getElementById('surnameErr').value;
	  if(checkEmpty(str)===false){
	      if(!/[^A-Za-z ]/.test(str)){
              document.getElementById('error_Surname').innerHTML="";
	      }	
          else{
              document.getElementById('error_Surname').innerHTML="* Only alphabets are allowed";  
         }
	  }
	  else{
		document.getElementById('error_Surname').innerHTML="* Only alphabets are allowed";   
	}
}

//checking phone number
function   checkPhone(){
	  var number=document.getElementById('phone').value;
	  
	  var mobile=/^0(6|7|8){1}[0-9]{1}[0-9]{7}$/;
	  if(mobile.test(number)){
           document.getElementById('error_Phone').innerHTML="";
	  }	
     else{
         document.getElementById('error_Phone').innerHTML="* Please enter valid cellphone number";  
     }		 
}

//company name

//checking email
function checkEmail(){
	var email=document.getElementById('emailErr').value;
	 var pattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	  if (pattern.test(email)) {
		 document.getElementById("err_email").innerHTML=""; 
	  }
	  else{
		 document.getElementById("err_email").innerHTML="* Wrong Email Address";  
	  }
}

function checkPassword(){


	
	if(document.getElementById('pswd').value!=document.getElementById('conPswd').value){

		document.getElementById('errorPassword').innerHTML="* Passwords do not match!";
	}
	else{
		document.getElementById('errorPassword').innerHTML="";
	}
	
}

//checking passwords
function checkPass(){
   var passw=document.getElementById('pswd').value;
   var conPassw=document.getElementById('conPswd').value;

	let pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&.])[A-Za-z\d$@$1%*?&.]{8,20}/;
	
	if(pattern.test(passw)) {
		
		document.getElementById('errorPass').innerHTML=""
	}
	else{
		document.getElementById('errorPass').innerHTML="Password should be at least 8 characters in length. Should include at least upper case letter, lowercase case letter, a number, and special character."
		
	}
	
   if(conPassw.length!=0){
	if(conPassw!=passw){

		document.getElementById('errorPassword').innerHTML="* Passwords do not match!";
		
	}
	else{
		
		document.getElementById('errorPassword').innerHTML="*";		
		
	}
  }
	

	
}

function clearMobile(){
    document.getElementById("nameM").value="";
    document.getElementById("surnameM").value="";
    document.getElementById("phoneM").value="";
    document.getElementById("emailM").value="";
    document.getElementById("CompNameM").value="";
    document.getElementById("pswdM").value="";
    document.getElementById("conPswdM").value="";
}

	
/*==========================================================================================================*/
</script>