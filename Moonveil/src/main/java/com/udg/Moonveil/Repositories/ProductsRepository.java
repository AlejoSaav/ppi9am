package com.udg.Moonveil.Repositories;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.udg.Moonveil.Models.ProductsModel;


@Repository
public interface ProductsRepository extends CrudRepository<ProductsModel, Long> {

    public abstract ArrayList<ProductsModel> findByCode(Integer code);

    public Optional<ArrayList<ProductsModel>> findProductByName(String name);
}
