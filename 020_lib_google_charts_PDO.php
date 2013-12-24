<?php
define("usuario_bdatos", "AAAAA");
define("password_bdatos", "BBBBB");
 define("bdatos", "Economia");
  define("tabla", "Gastos");
define("f_inicio", "2013-06-01");
define("f_fin", "2013-12-30");


//funciones de conexión y desconexión con la base de datos ----------------
function AbreBD_PDO(){
 try {
  $gbd = new PDO('mysql:host=localhost;dbname='.bdatos, usuario_bdatos, password_bdatos);
 } catch (PDOException $e) {
    print "¡Error!: " . $e->getMessage() . "<br/>";
    die();
 }
 return $gbd;
}

function CierraBD_PDO($gbd){
 $gbd = null;
}

//-------------------------------------------------------------------------

function EscribeGrafica_PDO(){
 $gbd = AbreBD_PDO();

 $sentencia = $gbd->prepare("SELECT * FROM ".tabla." WHERE fecha >= :f_inicio and fecha < :f_fin ;");

 $sentencia->bindValue(':f_inicio', f_inicio, PDO::PARAM_STR);
 $sentencia->bindValue(':f_fin', f_fin, PDO::PARAM_STR);

 if ($sentencia->execute()) {
  while ($registro = $sentencia->fetch()) {
   $luz = $registro['Luz'];
   $gas = $registro['Gas'];
   $agua = $registro['Agua'];
   $internet = $registro['Internet'];
   $otros = $registro['Otros'];
   $media = ($luz + $gas + $agua + $internet + $otros)/5;
   $fecha = TraduceMes(date('n',strtotime($registro['Fecha'])));
   echo "\t\t\t['".$fecha."',".$luz.",".$gas.",".$agua.",".$internet.",".$otros.",".$media."],\n";
  }
 }

 CierraBD_PDO($gbd);
}

function LlamaGoogle(){

[...]

?>
