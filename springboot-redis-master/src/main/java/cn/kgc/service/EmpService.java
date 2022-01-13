package cn.kgc.service;

import cn.kgc.entities.Emp;

/**
 * @Auther: zhangrunmin
 * @Date: 14/12/2021 16:47
 * @Description:
 */
public interface EmpService {
    public void add(Emp emp);

    public Object getEmpyById(Integer id);
}
