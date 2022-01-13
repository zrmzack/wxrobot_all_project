package cn.kgc.controller;

import lombok.extern.slf4j.Slf4j;
import org.assertj.core.util.Strings;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Set;

/**
 * @Auther: zhangrunmin
 * @Date: 14/12/2021 15:38
 * @Description:
 */
@RestController
@Slf4j
public class RedisController {

    @Autowired
    private RedisTemplate redisTemplate;

    @GetMapping("/redis/get/{key}")
    public Object get(@PathVariable("key") String key) {
        return redisTemplate.opsForValue().get(key);
    }

    @PostMapping("/redis/set/{key}/{value}")
    public Object set(@PathVariable("key") String key, @PathVariable("value") String value) {
        redisTemplate.opsForValue().set(key, value);
        return "success";
    }
    @CrossOrigin
    @PostMapping("/redis/add/{key}/{value}")
    public Object getall(@PathVariable("key") String key, @PathVariable("value") String value) {

        Set<String> keys = redisTemplate.keys("QandA");
        log.debug(String.valueOf(keys));
        redisTemplate.opsForHash().put("QandA", key, value);
        return "success";
    }

}
