<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de empleados</title>
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

        span {
            font-weight: bold;
        }

        .logo img {
            width: 150px;
            height: auto;
            display: block;
        }

        #contenido {
            margin: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
            text-align: center;
        }

        #crearEmpleado {
            background-color: #333;
            text-align: center;
            margin-bottom: 20px;
        }

        a.button {
            text-decoration: none;
            color: #fff;
            background-color: #db4435;
            padding: 10px 15px;
            border-radius: 4px;
            display: inline-block;
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

        .ver-detalle, .editar, .eliminar {
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
    </style>
</head>
<body>
    <nav>
        <ul>
            <li class="logo"><img src="Imagenes/Seele.png" alt="Logo de la empresa"></li>
            <li><a href="index.HTML.php">INICIO</a></li>
            <li><a href="Productos.HTML.php">PRODUCTOS</a></li>
            <li><a href="Empleados.HTML.php">EMPLEADOS</a></li>
            <li><a href="carrito.php">CARRITO</a></li>
        </ul>
    </nav>

    <div id="contenido">
        <h1>Listado de Empleados</h1>
        <div id="crearEmpleado">
            <a href="RegistrarEmpleado.html">Crear nuevo registro</a>
        </div>
        <table id="employeesTable">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre completo</th>
                    <th>Correo</th>
                    <th>Posicion</th>
                    <th>Edad</th>
                    <th>Opciones</th>
                </tr>
            </thead>
            <tbody> 
                <!-- Table body will be populated dynamically -->
            </tbody>
        </table>

        <script>
            const url = "http://localhost:8080/Employee";

            async function populateTableFromJSON(url) {
                cleanTableRows();
                try {
                    const response = await fetch(url);
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    const allEmployeesFromDB = await response.json();
                    const tableBody = document.querySelector("#employeesTable tbody");
                    allEmployeesFromDB.forEach(employee => {
                        const row = document.createElement("tr");
                        let idNumber = employee.id;
                        row.innerHTML = `
                            <td>${idNumber}</td>
                            <td contenteditable="false">${employee.name}</td>
                            <td contenteditable="false">${employee.email}</td>
                            <td contenteditable="false">${employee.position}</td>
                            <td contenteditable="false">${employee.age}</td>
                            <td>
                                <button type="button" class="btn btn-danger" onclick="deleteEmployeeButton('${idNumber}')">Eliminar</button>
                                <button type="button" class="btn btn-warning" onclick="editEmployee('${idNumber}')">Editar</button>
                            </td>
                        `;
                        tableBody.appendChild(row);
                    });
                } catch (error) {
                    console.error('There was a problem with the fetch operation:', error);
                }
            }

            populateTableFromJSON(url);

            function editEmployee(id) {
                let row = document.getElementById(id);
                ['name', 'email', 'position', 'age'].forEach((field, idx) => {
                    row.cells[idx + 1].contentEditable = 'true';
                });
                let editButton = row.cells[5].children[1];
                editButton.textContent = 'Guardar';
                editButton.onclick = function() {
                    saveEmployee(id);
                };
            }

            function saveEmployee(id) {
                let row = document.getElementById(id);
                const updatedEmployee = {
                    id: row.cells[0].textContent,
                    name: row.cells[1].textContent,
                    email: row.cells[2].textContent,
                    position: row.cells[3].textContent,
                    age: row.cells[4].textContent
                };

                fetch(`http://localhost:8080/Employee/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(updatedEmployee)
                })
                .then(response => response.json())
                .then(() => populateTableFromJSON(url))
                .catch(error => console.error('Failed to update employee:', error));
            }

            function deleteEmployeeButton(id) {
                if (confirm("Are you sure you want to delete this employee: " + id + "?")) {
                    fetch(`http://localhost:8080/Employee/delete-employee-by-id?id=${id}`, {
                        method: 'DELETE'
                    })
                    .then(response => response.ok ? populateTableFromJSON(url) : Promise.reject('Failed to delete'))
                    .catch(error => console.error('Error deleting employee:', error));
                }
            }

            function cleanTableRows() {
                const table = document.getElementById('employeesTable').tBodies[0];
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
