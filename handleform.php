<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="style.css">
<script src= "script.js"></script>
</head>

<a href = "home.html"><h1 class = "home"><img src=home.png></h1></a>

<h1><center><img src=bethsportfolio.png></center></h1>


<h2><center> Your Login Details</center></h2>


<body><center><h4>
Your Username is: <?php echo htmlspecialchars($_POST['user']);?>
<br>
Your Password is: <?php echo htmlspecialchars($_POST['pass']);?>
</center></h4>
</body>