<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = $_POST['input'];
    file_put_contents('../input_curl.txt', $input);
    $command = "python ../app.py ../input_curl.txt 2>&1";
    $output = shell_exec($command);
    if ($output === null) {
        $output = "No output from python script.";
    }
    $output_encoded = urlencode($output);
    header("Location: ../Fronet-End/index2.php?result=$output_encoded");
    exit;
} else {
    echo "error please send a request with arguments";
}
?>

