<?php

//hay que renombrar como lib.php

//funciones de conexión y desconexión con la base de datos ----------------
function AbreBD(){
 if(!$conn = mysql_connect("localhost","usuario_bdatos","password_bdatos")){
  die("Se ha producido un error conectando con la BD");
 }
 if(!mysql_select_db("Economia",$conn)){
  die("Se ha producido un error seleccionando la BD");
 }
 mysql_query("SET NAMES 'utf8'",$conn);
 return $conn;
}

function CierraBD($identificador){
 mysql_close($identificador);
}
//-------------------------------------------------------------------------

function EscribeGrafica(){
 $ssql = "SELECT * FROM Gastos ";
 $ssql = $ssql."WHERE Fecha >='2013-06-01' AND Fecha < '2013-12-30';";

 //echo $ssql;

 $conn = AbreBD();
 $query = mysql_query($ssql,$conn);

 while ($registro = mysql_fetch_assoc($query)){
  $luz = $registro['Luz'];
  $gas = $registro['Gas'];
  $agua = $registro['Agua'];
  $internet = $registro['Internet'];
  $otros = $registro['Otros'];
  $media = ($luz + $gas + $agua + $internet + $otros)/5;
  $fecha = TraduceMes(date('n', strtotime($registro['Fecha'])));
  echo "\t\t\t['".$fecha."',".$luz.",".$gas.",".$agua.",".$internet.",".$otros.",".$media."],\n";
 }

 mysql_free_result($query);
 CierraBD($conn);
}

function LlamaGoogle(){
 echo " <script type=\"text/javascript\" src=\"https://www.google.com/jsapi\"></script>\n";
 echo "   <script type=\"text/javascript\">\n";
 echo "        google.load('visualization', '1', {packages: ['corechart']});\n";
 echo "   </script>\n";
 echo "   <script type=\"text/javascript\">\n";
 echo "    function drawVisualization() {\n";
 echo "     var data = google.visualization.arrayToDataTable([\n";
 echo "            ['Mes'      ,'Luz','Agua','Gas','Internet','Otros','Media'],\n";
 //echo "           ['Enero'   ,  130,   100,  300,       145,    120,     100],\n";
 //echo "           ['Febrero ',  140,   110,  310,       155,    130,     110],\n";
 EscribeGrafica();
 echo "     ]);\n";

 echo "     var options = {\n";
 echo "           title : 'Gastos mensuales del piso',\n";
 echo "           vAxis: {title: \"Euros\"},\n";
 echo "           hAxis: {title: \"Mes\"},\n";
 echo "           seriesType: \"bars\",\n";
 echo "           series: {5: {type: \"line\"}}\n";
 echo "     };\n";

 echo "     var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));\n";
 echo "         chart.draw(data, options);\n";
 echo "     }\n";
 echo "     google.setOnLoadCallback(drawVisualization);\n";
 echo "   </script>\n";
}

function TraduceMes($num_mes){
 switch ($num_mes) {
    case 1:
        return "Enero";
        break;
    case 2:
        return "Febrero";
        break;
    case 3:
        return "Marzo";
        break;
    case 4:
        return "Abril";
        break;
    case 5:
        return "Mayo";
        break;
    case 6:
        return "Junio";
        break;
    case 7:
        return "Julio";
        break;
    case 8:
        return "Agosto";
        break;
    case 9:
        return "Septiembre";
        break;
    case 10:
        return "Octubre";
        break;
    case 11:
        return "Noviembre";
        break;
    case 12:
        return "Diciembre";
        break;
 }
}
?>
