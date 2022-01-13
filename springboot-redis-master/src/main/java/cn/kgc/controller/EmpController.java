package cn.kgc.controller;

import cn.kgc.entities.Emp;
import cn.kgc.service.EmpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * @Auther: zhangrunmin
 * @Date: 15/12/2021 08:53
 * @Description:
 */
@RestController
public class EmpController {
    @Autowired
    public RedisTemplate redisTemplate;
    @Autowired
    private EmpService empService;

    @PostMapping("/emp")
    public String addEmp(Emp emp) {
        empService.add(emp);
        return "add success";
    }

    @GetMapping("/emp/{id}")
    public Object getEmp(@PathVariable("id") Integer id) {
        ExecutorService es = Executors.newFixedThreadPool(200);
        for (int i = 0; i < 500; i++) {
            es.submit(new Runnable() {
                @Override
                public void run() {
                    empService.getEmpyById(id);
                }
            });
        }

        return empService.getEmpyById(id);
    }

}
