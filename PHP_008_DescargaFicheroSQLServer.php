<?php

//importamos nuestra librería con las funciones de conexion a la base de datos, securización, etcétera

//construimos la sentencia SQL, por ejemplo:

$ssql = “SELECT Fichero FROM TFicheros WHERE IDFichero = 3″

//abrimos la conexion, y ejecutamos la query

$conexion = AbreBD();

$consulta = mssql_query($ssql, $conexion);

$registro = mssql_fetch_assoc($consulta);

$archivo = $registro["Fichero"];

//pasamos los header del tipo de fichero… esto habrá que cambiarlo en funcion del fichero

header(‘Content-type: application/pdf’);

header(‘Content-Disposition: attachment; filename=Fichero.pdf’);

echo $archivo;

//cerramos todo

mssql_free_result($consulta);

CierraBD($conexion);

?>
