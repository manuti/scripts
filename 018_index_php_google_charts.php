<!-- rename to index.php -->
<?php
 include ("lib.php");
 $conn = AbreBD();
 CierraBD($conn);
?>

<!doctype html>
<html lang=es>

 <head>
  <meta charset=utf-8>
  <title>Economia</title>
  <?php LlamaGoogle(); ?>
 </head>

 <body>
  <div id="chart_div" style="width: 900px; height: 500px;"></div>
 </body>
</html>
