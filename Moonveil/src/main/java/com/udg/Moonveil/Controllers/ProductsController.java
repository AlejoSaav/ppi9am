package com.udg.Moonveil.Controllers;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.udg.Moonveil.Models.ProductsModel;
import com.udg.Moonveil.Services.ProductsService;

@RestController
@RequestMapping("/Product")
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
    public Optional<ArrayList<ProductsModel>> findByCode(@RequestParam("name")String name){
        return productsService.findByName(name);
    }

    @DeleteMapping("/delete-product-by-id")
    public String deleteProductById(@RequestParam("id") Long id){
        return productsService.deleteProductById(id);
    }


}
