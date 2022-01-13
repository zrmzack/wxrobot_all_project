package redisspringboot;

import org.junit.jupiter.api.Test;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;

import java.util.*;

@SpringBootTest
@SpringBootConfiguration
class DemoApplicationTests {

    @Test
    public void contextLoads(RedisConnectionFactory f) {
        RedisTemplate redisTemplate = new RedisTemplate();
        List<Map<Object, Object>> list = new ArrayList<>();

//        Set<String> keys = redisTemplate.keys();
//        System.out.println(keys);
    }


//    @Test
//    public void contextLoad1s() {
//
//        for (String key : keys) {
//            HashMap<Object, Object> map = new HashMap<>();
//            //String类型的键值获取
//            if (redisTemplate.type(key).code() == "string") {
//                Object value = redisTemplate.opsForValue().get(key);
//
//                map.put("key", key);
//                map.put("value", value);
//                list.add(map);
//            }
//            //zset类型的键值获取
//            if (redisTemplate.type(key).code() == "zset") {
//                Object value = redisTemplate.opsForZSet().range(key, 0, -1);
//                map.put("key", key);
//                map.put("value", value);
//                list.add(map);
//            }
//            //set类型的键值获取
//            if (redisTemplate.type(key).code() == "set") {
//                Object value = redisTemplate.opsForZSet().range(key, 0, -1);
//                map.put("key", key);
//                map.put("value", value);
//                list.add(map);
//            }
//            //list类型的键值获取
//            if (redisTemplate.type(key).code() == "list") {
//                Object value = redisTemplate.opsForZSet().range(key, 0, -1);
//                map.put("key", key);
//                map.put("value", value);
//                list.add(map);
//            }
//            //hash类型的键值获取
//            if (redisTemplate.type(key).code() == "hash") {
//                Object value = redisTemplate.opsForZSet().range(key, 0, -1);
//                map.put("key", key);
//                map.put("value", value);
//                list.add(map);
//            }
//        }
//        System.out.println(list);
//    }


}
