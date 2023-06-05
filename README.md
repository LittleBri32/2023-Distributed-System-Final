測試test data是否有insert到db

#進到container的mysql
docker run -it --rm --network docker-envoyproxy-menu-main_envoymesh mysql:5.7 sh -c 'exec mysql -h mysql-server -P 3306 -u root -psecret'

#sql query
USE ds_prj
SELECT * FROM ticket_order;
