package com.udg.Moonveil.Controllers;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

import com.udg.Moonveil.Models.ProductsModel;
import com.udg.Moonveil.Services.ProductsService;

public class ProductsController {
    @Autowired
    ProductsService productsService;

    //Get
    @GetMapping
    public ArrayList<ProductsModel> findAllProducts(){
        return productsService.findAllProducts();
    }
    //Post
    @PostMapping
    public ProductsModel saveProduct(@RequestBody ProductsModel product){
        return productsService.saveProduct(product);
    }

    //Editar
    @PutMapping
    public ProductsModel updateProduct(@RequestBody ProductsModel product){
        return productsService.saveProduct(product);
    }


    //Buscar por código
    @GetMapping(path = "/find-by-code")
    public ArrayList<ProductsModel> findByCode(@RequestParam("code")Integer code){
        return productsService.findByCode(code);
    }
    //Buscar por nombre
    @GetMapping(path = "/find-by-name")
    public ArrayList<ProductsModel> findByCode(@RequestParam("name")String name){
        return productsService.findByName(name);
    }


}
