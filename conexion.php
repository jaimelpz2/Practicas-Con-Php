<?php 

$conexion = mysqli_connect('localhost','root','123','matanga') or die(mysql_error($mysqli));

insertar($conexion);

function insertar($conexion){
// variables de lado izquierdo declaradas en el html y del derecho de la BSD
	$username= $_POST['gansito'];
	$email= $_POST['donal'];
	$password= $_POST['refresco'];

	$consulta="INSERT INTO registro(gansito,donal,refresco) VALUES ('$gansito','$donal','$refresco')";
	mysqli_query($conexion, $consulta);
	mysqli_close($conexion);
}


?>