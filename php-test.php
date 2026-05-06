<?php
// Set the timezone (adjust if needed)
date_default_timezone_set('Australia/Brisbane');

// Get system information
$date = date('d/m/Y');
$time = date('H:i:s');
$computerName = gethostname();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>System Info</title>
</head>
<body>
    <h1>System Information</h1>
    <p><strong>Date:</strong> <?php echo $date; ?></p>
    <p><strong>Time:</strong> <?php echo $time; ?></p>
    <p><strong>Computer Name:</strong> <?php echo $computerName; ?></p>
</body>
</html>
