package com.udg.Moonveil.Services;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.udg.Moonveil.Models.ProductsModel;
import com.udg.Moonveil.Repositories.ProductsRepository;

@Service
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

    public Optional<ArrayList<ProductsModel>> findByName(String name){
        return productsRepository.findProductByName(name);
    }

    public ArrayList<ProductsModel> findByCode(Integer code){
        return productsRepository.findByCode(code);
    }

    public Optional<ProductsModel> findProductById(Long id){
        return productsRepository.findById(id);
    }

    public String deleteProductById(Long id){

        if(findProductById(id).isPresent()){
            productsRepository.deleteById(id);
            return "student deleted successfully";
        }else {
            return "student with id="+ id+ " not foud";
        }
    }


    public Optional<ArrayList<ProductsModel>> findProductByName(String name){
        return productsRepository.findProductByName(name);


}

}