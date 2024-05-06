package com.udg.Moonveil.Services;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;

import com.udg.Moonveil.Models.ProductsModel;
import com.udg.Moonveil.Repositories.ProductsRepository;

public class ProductsService {
    @Autowired
    ProductsRepository productsRepository;

    //Obtener todo
    public ArrayList<ProductsModel> findAllProducts(){
        return (ArrayList<ProductsModel>) productsRepository.findAll();
    }
    //Guardar
    public ProductsModel saveProduct(ProductsModel product){
        return productsRepository.save(product);
    }

    public ArrayList<ProductsModel> findByName(String name){
        return productsRepository.findByName(name);
    }

    public ArrayList<ProductsModel> findByCode(Integer code){
        return productsRepository.findByCode(code);
    }


}
