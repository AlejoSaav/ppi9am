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

import com.udg.Moonveil.Models.EmployeesModel;
import com.udg.Moonveil.Services.EmployeesService;

@RestController
@RequestMapping("/Employee")
public class EmployeesController {
    @Autowired
    EmployeesService employeesService;

    //Get
    @GetMapping
    public ArrayList<EmployeesModel> findAllEmployees(){
        return employeesService.findAllEmployees();
    }
    //Post
    @PostMapping
    public EmployeesModel saveEmployee(@RequestBody EmployeesModel employee){
        return employeesService.saveEmployee(employee);
    }

    //Editar
    @PutMapping
    public EmployeesModel editEmployee(@RequestBody EmployeesModel employee){
        return employeesService.editEmployee(employee);
    }

    //Buscar por nombre
    @GetMapping(path = "/findEmployeeByName{name}")
    public Optional<ArrayList<EmployeesModel>> findEmployeeByName(@RequestParam("name")String name){
        return employeesService.findEmployeeByName(name);
    }

    @DeleteMapping("/delete-employee-by-id")
    public String deleteEmployeeById(@RequestParam("id") Long id){
        return employeesService.deleteEmployeeById(id);
    }

}
