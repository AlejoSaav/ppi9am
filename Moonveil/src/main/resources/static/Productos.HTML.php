<html>
    
<head>
    <title>Lista de productos</title>
    <style>
        
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: url('Imagenes/Fondo2.png') no-repeat center center fixed;
            background-size: cover; 
        }

       
        nav {
            background-color: #333;
            color: #fff;
            padding: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        
        ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }

        li {
            margin-right: 15px;
        }

        a {
            text-decoration: none;
            color: #fff;
            font-weight: bold;
            padding: 10px;
        }

        
        #contenido {
            margin: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #crearProducto {
                background-color: #333;
                text-align: center;
                margin-bottom: 20px;
            }

        h1 {
            color: #333;
            text-align: center;
        }

        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #d4d4d4;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #ededed;
            text-align: center;
        }

        
        .ver-detalle, .editar,.comprar, .eliminar {
            text-align: center;
        }

        .ver-detalle a, .editar a, .eliminar a {
            color: #fff;
            background-color: #db4435;
            padding: 6px 10px;
            text-decoration: none;
            border-radius: 4px;
            display: inline-block;
        }
        .comprar a {
            color: #fff;
            background-color: #db4435;
            padding: 6px 10px;
            text-decoration: none;
            border-radius: 4px;
            display: inline-block;
        }

        
        #regresarInicio {
            text-align: left;
            margin-top: 20px;
        }

        #regresarInicio a {
            color: #fff;
            background-color: #db4435;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 4px;
            display: inline-block;
            transition: background-color 0.3s;
        }
        
                
        .logo img {
                    width: 150px; 
                    height: auto; 
                    display: block; 
                }
    </style>
    
    <script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>

    <script>
        $(document).ready(function () {
            $('#editarForm').submit(function (event) {
                event.preventDefault();
                handleFormSubmission();
            });

            $('#regresarListado').click(function (event) {
                event.preventDefault();
                $('#editarFormContainer').hide();
            });

            // Initially, hide the edit form
            $('#editarFormContainer').hide();
        });

        function editarProducto(id) {
            $.ajax({
                url: 'obtener_producto.php?id=' + id,
                type: 'GET',
                dataType: 'json',
                success: function (productoData) {
                    $('#id').val(productoData.ID);
                    $('#Nombre').val(productoData.Nombre);
                    $('#Codigo').val(productoData.Codigo);
                    $('#Descripcion').val(productoData.Descripcion);
                    $('#Costo').val(productoData.Costo);
                    $('#Stock').val(productoData.Stock);
                    // Agrega más campos si es necesario
                    $('#editarFormContainer').show();
                },
                error: function () {
                    mostrarMensaje('Error al obtener la información del empleado', false);
                }
            });
        }

        function mostrarListado() {
            $('#editarFormContainer').hide();
            // Puedes redirigir a la página de listado si es necesario
        }

        function mostrarMensaje(mensaje, exitoso = false) {
            const mensajeContainer = $('#mensaje-container');
            mensajeContainer.html(`<div class="${exitoso ? 'exito' : 'error'}">${mensaje}</div>`);
            setTimeout(() => {
                mensajeContainer.html('');
            }, 5000);
        }

        function handleFormSubmission() {
            const formData = $('#editarForm').serialize(); // Obtén los datos del formulario

            $.ajax({
                url: 'actualizar_producto.php', // Reemplaza con la ruta correcta a tu script de actualización
                type: 'POST',
                data: formData,
                dataType: 'json',
                success: function (response) {
                    if (response.success) {
                        mostrarMensaje('Producto actualizado exitosamente', true);
                        mostrarListado(); // Otra función para volver al listado si es necesario
                    } else {
                        mostrarMensaje(response.error || 'Error al actualizar producto', false);
                    }
                },
                error: function () {
                    mostrarMensaje('Error al enviar la solicitud de actualización', false);
                }
            });
        }

        $(document).ready(function() {
            $(".eliminarProducto").on("click", function(e) {
                e.preventDefault();
                var idProducto = $(this).data("id");
                var confirmar = confirm("¿Estás seguro de que deseas eliminar este producto?");

                if (confirmar) {
                    // Llamada AJAX
                    $.ajax({
                        type: "POST",
                        url: "eliminar_producto.php",
                        data: { idProducto: idProducto },
                        success: function(response) {
                            if (response === "success") {
                                // Si la eliminación es exitosa, oculta la fila
                                $(e.target).closest("tr").hide();
                            } else {
                                alert("Error al eliminar el registro");
                            }
                        }
                    });
                }
            });
        });
    </script>
</head>
<body>

    <nav>
        <ul>
            <li class="logo"><img src="Imagenes/Seele.png"></li>
            <li><a href="index.HTML.php">INICIO</a></li>
            <li><a href="Productos.HTML.php">PRODUCTOS</a></li>
            <li><a href="Empleados.HTML.php">EMPLEADOS</a></li>
            <li><a href="carrito.php">CARRITO</a></li>
        </ul>
    </nav>


<div id="contenido">
    <h1>Listado de Productos</h1>

    <div id="crearProducto">
        <a href="formulario_alta_producto.php">Crear nuevo producto</a>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Código</th>
                <th>Descripción</th>
                <th>Costo</th>
                <th>Stock</th>
                <th>Editar</th>
                <th>Borrar producto</th>
            </tr>
        </thead>
        <tbody>
        <?php
                    require "Funciones/conectaProductos.php";
                    $con = conecta();

                    $sql = "SELECT * FROM Productos WHERE status = 1 AND Eliminado = 0";
                    $res = $con->query($sql);

                    while ($row = $res->fetch_array()) {
                        $ID = $row["ID"];
                        $Nombre = $row["Nombre"];
                        $Codigo = $row["Codigo"];
                        $Descripcion = $row["Descripcion"];
                        $Costo = $row["Costo"];
                        $Stock = $row["Stock"];

                        echo "<tr>";
                        echo "<td>$ID</td>";
                        echo "<td>$Nombre</td>";
                        echo "<td>$Codigo</td>";
                        echo "<td class='ver-detalle'><a href='detalle_producto.php?id=$ID'>Ver detalle</a></td>";
                        echo "<td>$Costo</td>";
                        echo "<td>$Stock</td>";

                        echo "<td class='editar'><a href='javascript:void(0);' onclick='editarProducto($ID)'>Editar</a></td>";
                        echo "<td class='eliminar'><a class='eliminarProducto' data-id='$ID' href='#'>Eliminar</a></td>";

                        echo "</tr>";
                    }
                ?>
        </tbody>
    </table>

    
    <div id="editarFormContainer">
            <h2>Edición de productos</h2>
            <form id="editarForm">
                <input type="hidden" id="id" name="id" />
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre">

                <label for="Codigo">Codigo:</label>
                <input type="text" id="Codigo" name="Codigo" onBlur="validarProducto()">

                <label for="Descripcion">Descripción:</label>
                <input type="text" id="Descripcion" name="Descripcion">

                <label for="Costo">Costo:</label>
                <input type="number" id="Costo" name="Costo">

                <label for="Stock">Stock:</label>
                <input type="number" id="Stock" name="Stock">

                <div id="mensaje-container"></div>
                <input type="submit" value="Guardar cambios">
            </form>
            <a href="#" id="regresarListado">Regresar al listado</a>
        </div>

        <div id="regresarInicio">
            <a href="Bienvenida.HTML.php">Regresar al Inicio</a>
        </div>
</div>
</body>
</html>