package com.udg.Moonveil.Repositories;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.udg.Moonveil.Models.EmployeesModel;

@Repository
public interface EmployeesRepository extends CrudRepository<EmployeesModel, Long>{

    public Optional<ArrayList<EmployeesModel>> findEmployeeByName(String name);

}
