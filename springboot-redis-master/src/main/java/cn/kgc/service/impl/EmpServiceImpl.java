package cn.kgc.service.impl;

import cn.kgc.entities.Emp;
import cn.kgc.mapper.EmpMapper;
import cn.kgc.service.EmpService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

/**
 * @Auther: zhangrunmin
 * @Date: 14/12/2021 16:48
 * @Description:
 */
@Service
@Slf4j
public class EmpServiceImpl implements EmpService {
    @Autowired
    private RedisTemplate redisTemplate;
    @Resource
    private EmpMapper empMapper;

    @Override
    public void add(Emp emp) {
        empMapper.insert(emp);
    }

    @Override
    public Object getEmpyById(Integer id) {
        String key = "user:" + id;
        Object obj = redisTemplate.opsForValue().get(key);
        if (obj == null) {
            synchronized (this.getClass()) {
                obj = redisTemplate.opsForValue().get(key);
                if (obj == null) {
                    log.debug("------查询数据库中------");
                    Emp emp = empMapper.selectByPrimaryKey(id);
                    redisTemplate.opsForValue().set(key, emp);
                    return emp;
                } else {
                    log.debug("----缓存同步---");
                    return obj;
                }
            }

        } else {
            log.debug("------缓存中获取------");
            return obj;
        }
    }
}
