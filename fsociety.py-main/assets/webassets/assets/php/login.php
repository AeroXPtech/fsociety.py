<?php
session_start();
$username = $_POST['username'] ?? '';

echo 'Successfully Logged in' . $_POST['username'];

if($username == '') {
    $_SESSION['logged_in'] = true;
    echo 'For Privacy Reasons Is Every Password 
    webcore2dot0@webcore.com Please
    Visit https://aeroxptech.github.io/fsociety.py/index.html you are still logged in';
    exit;
}