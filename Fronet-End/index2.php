<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>converter</title>
    <link rel="stylesheet" href="style2.css" />
</head>
<body>
    <textarea id="ksj" class="ksj"><?php
        if (isset($_GET['result'])) {
            echo htmlspecialchars(urldecode($_GET['result']));
        } else {
            echo "error";
        }
    ?></textarea>
    <br>
    <button onclick="textCopy()">copy</button>

    <script src="script.js"></script>
</body>
</html>
