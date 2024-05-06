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
        <a href="RegistrarProducto.html">Crear nuevo producto</a>
    </div>

    <table id="productsTable">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Código</th>
                <th>Stock</th>
                <th>Precio</th>
                <th>Opciones</th>
            </tr>
        </thead>
        <tbody>
        <script>
            const url = "http://localhost:8080/Product";

            async function populateTableFromJSON(url) {
                cleanTableRows();
                try {
                    const response = await fetch(url);
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    const allProductsFromDB = await response.json();
                    const tableBody = document.querySelector("#productsTable tbody");
                    allProductsFromDB.forEach(product => {
                        const row = document.createElement("tr");
                        let idNumber = product.id;
                        row.innerHTML = `
                            <td>${idNumber}</td>
                            <td contenteditable="false">${product.name}</td>
                            <td contenteditable="false">${product.description}</td>
                            <td contenteditable="false">${product.stock}</td>
                            <td contenteditable="false">${product.code}</td>
                            <td contenteditable="false">${product.price}</td>
                            <td>
                                <button type="button" class="btn btn-danger" onclick="deleteProductButton('${idNumber}')">Eliminar</button>
                                <button type="button" class="btn btn-warning" onclick="editProduct('${idNumber}')">Editar</button>
                            </td>
                        `;
                        tableBody.appendChild(row);
                    });
                } catch (error) {
                    console.error('There was a problem with the fetch operation:', error);
                }
            }

            populateTableFromJSON(url);

            function editProduct(id) {
                let row = document.getElementById(id);
                ['name', 'description', 'stock', 'code', 'price'].forEach((field, idx) => {
                    row.cells[idx + 1].contentEditable = 'true';
                });
                let editButton = row.cells[5].children[1];
                editButton.textContent = 'Guardar';
                editButton.onclick = function() {
                    saveProduct(id);
                };
            }

            function saveProduct(id) {
                let row = document.getElementById(id);
                const updatedEmployee = {
                    id: row.cells[0].textContent,
                    name: row.cells[1].textContent,
                    description: row.cells[2].textContent,
                    stock: row.cells[3].textContent,
                    code: row.cells[4].textContent,
                    price: row.cells[5].textContent
                };

                fetch(`http://localhost:8080/Product/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(updatedProduct)
                })
                .then(response => response.json())
                .then(() => populateTableFromJSON(url))
                .catch(error => console.error('Failed to update product:', error));
            }

            function deleteProductButton(id) {
                if (confirm("Are you sure you want to delete this product: " + id + "?")) {
                    fetch(`http://localhost:8080/Product/delete-product-by-id?id=${id}`, {
                        method: 'DELETE'
                    })
                    .then(response => response.ok ? populateTableFromJSON(url) : Promise.reject('Failed to delete'))
                    .catch(error => console.error('Error deleting product:', error));
                }
            }

            function cleanTableRows() {
                const table = document.getElementById('productsTable').tBodies[0];
                while (table.rows.length > 0) {
                    table.deleteRow(0);
                }
            }
        </script>

        <div id="regresarInicio">
            <a href="index.HTML.php">Regresar al Inicio</a>
        </div>
</div>
</body>
</html>