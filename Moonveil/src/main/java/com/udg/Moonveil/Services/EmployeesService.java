package com.udg.Moonveil.Services;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.udg.Moonveil.Models.EmployeesModel;
import com.udg.Moonveil.Repositories.EmployeesRepository;

@Service
public class EmployeesService {
    @Autowired
    EmployeesRepository employeesRepository;

    //Obtener todo
    public ArrayList<EmployeesModel> findAllEmployees(){
        return (ArrayList<EmployeesModel>) employeesRepository.findAll();
    }
    //Guardar
    public EmployeesModel saveEmployee(EmployeesModel employee){
        return employeesRepository.save(employee);
    }
    
    public EmployeesModel editEmployee(EmployeesModel employee){
        return employeesRepository.save(employee);
    }

    public ArrayList<EmployeesModel> getAllEmployees(){
        return(ArrayList<EmployeesModel>) employeesRepository.findAll();
    }

    public Optional<EmployeesModel> findEmployeeById(Long id){
        return employeesRepository.findById(id);
    }

    public String deleteEmployeeById(Long id){

        if(findEmployeeById(id).isPresent()){
            employeesRepository.deleteById(id);
            return "student deleted successfully";
        }else {
            return "student with id="+ id+ " not foud";
        }
    }

    public Optional<ArrayList<EmployeesModel>> findEmployeeByName(String name){
        return employeesRepository.findEmployeeByName(name);
    }
}
