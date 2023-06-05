## 測試test data是否有插入到db

先進到service1送出一筆訂單

**1. 進到container的mysql**

```bash
docker run -it --rm --network docker-envoyproxy-menu-main_envoymesh mysql:5.7 sh -c 'exec mysql -h mysql-server -P 3306 -u root -psecret'
```

**2. sql query**
```
USE ds_prj
SELECT * FROM ticket_order;
```

