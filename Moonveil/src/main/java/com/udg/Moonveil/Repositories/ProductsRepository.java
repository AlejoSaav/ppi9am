package com.udg.Moonveil.Repositories;

import java.util.ArrayList;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.udg.Moonveil.Models.ProductsModel;


@Repository
public interface ProductsRepository extends CrudRepository<ProductsModel, Long> {

    public abstract ArrayList<ProductsModel> findByCode(Integer code);

    public abstract ArrayList<ProductsModel> findByName(String name);
}
