<?php 
    header("Content-Type: application/json; charset=utf-8");

    #$data =file_get_contents('php://input');

    $data = '{"side":"longentry"}';
    #$data = '{"side":"longexit"}';
    #$data = '{"side":"shortentry"}';
    #$data = '{"side":"shortexit"}';

    $command = "python3 /var/AutoBinance_dev/main_seannie.py ". escapeshellarg($data);
    exec($command, $output, $return_var);
    $json_array = json_encode($output);
    echo $json_array

?>