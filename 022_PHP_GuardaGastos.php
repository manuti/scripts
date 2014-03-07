function GuardaGastos($Supermercado,$Ocio,$Libros,$Cañas,$Viajes,$Otros){
 $gbd = AbreBD_PDO();
 $sentencia = $gbd->prepare("INSERT INTO ".tablaEscrituras." (Fecha, Alquiler, Transporte, Supermercado, Ocio, Libros, Cañas, Viajes, Otros) $

 $sentencia->bindValue(':g_su', $Supermercado, PDO::PARAM_STR);
 $sentencia->bindValue(':g_oc', $Ocio, PDO::PARAM_STR);
 $sentencia->bindValue(':g_li', $Libros, PDO::PARAM_STR);
 $sentencia->bindValue(':g_ca', $Cañas, PDO::PARAM_STR);
 $sentencia->bindValue(':g_vi', $Viajes, PDO::PARAM_STR);
 $sentencia->bindValue(':g_ot', $Otros, PDO::PARAM_STR);

 $sentencia->execute();
 CierraBD_PDO($gbd);
}
