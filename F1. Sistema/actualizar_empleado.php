<?php
require "Funciones/conecta.php";

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $con = conecta();
    $id = $con->real_escape_string($_POST['id']);
    $nombre = $con->real_escape_string($_POST['nombre']);
    $correo = $con->real_escape_string($_POST['correo']);
    

   
    $correoExistente = validarCorreoExistente($con, $correo, $id);
    if ($correoExistente) {
        echo json_encode(array('success' => false, 'error' => 'El correo ya existe en la base de datos'));
        exit();
    }

    
    $sql = "UPDATE Empleados SET Nombre = '$nombre', Correo = '$correo' WHERE ID = $id";
    $res = $con->query($sql);

    if ($res) {
        echo json_encode(array('success' => true));
    } else {
        echo json_encode(array('success' => false, 'error' => 'Error al actualizar empleado'));
    }
} else {
    echo json_encode(array('success' => false, 'error' => 'Método no permitido'));
}

function validarCorreoExistente($con, $correo, $id) {
    $sql = "SELECT COUNT(*) as count FROM Empleados WHERE Correo = '$correo' AND ID != $id";
    $res = $con->query($sql);

    if ($row = $res->fetch_array()) {
        return $row['count'] > 0;
    }

    return false;
}
?>