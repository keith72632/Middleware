<html>
  <head>
    <title>PHP Test</title>
    <style type="text/css" media="screen">
      *{
	color: blue;
	}
      tr{
        border:1px solid black; 
        }
      th{
	border:1px solid black;
	}
      td {
	text-align:center;
        }
    </style>
  </head>
  <body>
    <?php
            $host = "192.168.0.183";
	    $port = 8888;

	    $removable = array("[", "]");

	    set_time_limit(0);

            $socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("no sock\n");

	    $result = socket_connect($socket, $host, $port) or die("Socket could not connect\n");

	    $input = socket_read($socket, 1024) or die("Could not read data\n");

	    $pre_explode_string = str_replace($removable, "", $input);
	    $output = explode(",", $pre_explode_string);

	    $E9_Temp = $output[0];
	    $E10_Temp = $output[1];
	    $E11_Temp = $output[2];
	    $E3_Temp = $output[3];
	    $E4_Temp = $output[4];
	    $E5_Temp = $output[5];
	    $E6_Temp = $output[6];
	    $E7_Temp = $output[7];
	    $E8_Temp = $output[8];
	    socket_close($result);
	    socket_close($socket);
    ?>

    <h1>Pump Diagnostics</h1>
    <table style="width:45%">
      <tr>
        <th style="border:1px solid black">Pumps</th>
        <th style="border:1px solid black">Pump Temperature</th>
      </tr>
      <tr>
        <th>High Service E9</th>
        <td><?php echo $E9_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E10</th>
        <td><?php echo $E10_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E11</th>
        <td><?php echo $E11_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E3</th>
        <td><?php echo $E3_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E4</th>
        <td><?php echo $E4_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E5</th>
        <td><?php echo $E5_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E6</th>
        <td><?php echo $E6_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E7</th>
        <td><?php echo $E7_Temp . "F"; ?></td>
      </tr>
      <tr>
        <th>High Service E8</th>
        <td><?php echo $E8_Temp . "F"; ?></td>
      </tr>

    </table>

  </body>
</html>
