<html>
<head>
    <title>Moonveil</title>
    <?php
    
    $banners = glob('banners/*.{jpg,jpeg,png,gif}', GLOB_BRACE);

    
    $imagenAleatoria = $banners[array_rand($banners)];
    ?>
    
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
        .producto {
            background-color: #fff; 
            border-radius: 8px; 
            padding: 15px; 
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); 
        }
        #cerrar-sesion {
        margin-right: auto;
        
         }

         #banner {
        width: 50%;
        max-height: 200px; 
        object-fit: auto; 
        margin-bottom: 20px;
    }

    .fondo-blanco {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%; 
        height: 100%;
        background-color: white;
        z-index: -1; 
        opacity: 0.7; 
}
    
    </style>
</head>
<body>

    
    <nav>
        <ul>
            <li class="logo"><img src="Imagenes/Seele.png"></li>
            <li><a href="index.HTML.php">INICIO</a></li>
            <li><a href="Productos.HTML.php">PRODUCTOS</a></li>
            <li><a href="Empleados.html.php">EMPLEADOS</a></li>
            <li><a href="carrito.php">CARRITO</a></li>
        </ul>
    </nav>

    
    <div class="fondo-blanco"></div>

<div style="text-align: center; margin-top: 50px;">
    <h1 style="color: #333;">Bienvenido a Moonveil</h1>
    <img id="banner" src="<?php echo $imagenAleatoria; ?>" alt="Banner Aleatorio">
    <h2>Productos Destacados</h2>
</div>
 
</div>

</body>
</html>