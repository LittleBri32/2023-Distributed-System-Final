# Ticketing System with Envoy

<br/>

## Run
Please make sure Docker is installed and running.

<br/>

Build the containers.

    docker-compose build --pull

Start all the containers.

    docker-compose up -d

Show all the running docker containers.

    docker-compose ps

Run the server.

    python3 service.py

<br/>

## Database

Docker Desktop > Containers > mysql-server > Terminal

    exec mysql -h mysql-server -P 3306 -u root -psecret

Query

    USE ds_prj
    SELECT * FROM ticket_order;

<br/>

## Load Balancing
    
Scale service3 to 3 instances.

    docker-compose up --scale service3=3 -d
    
Show all the running docker containers.

    docker-compose ps

Send request to service3 multiple times.

    docker-compose exec -T front-envoy bash -c "\
                   curl -s http://localhost:8080/service/3 \
                   && curl -s http://localhost:8080/service/3 \
                   && curl -s http://localhost:8080/service/3" \
                   | grep hostname
