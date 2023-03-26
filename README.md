## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/nginx-flask-mongo)

### Python/Flask application with Nginx proxy and a Mongo database

Project structure:
```
.
├── compose.yaml
├── flask
│   ├── Dockerfile
│   ├── requirements.txt
│   └── server.py
├── nginx
│   └── nginx.conf
├── react
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   └── App.js
```

[_compose.yaml_](compose.yaml)
```
services:
  web:
    build: app
    ports:
    - 80:80
  backend:
    build: flask
    ...
  mongo:
    image: mongo
  frontend:
    build: App

```
The compose file defines an application with four services `web`, `backend`, `frontend` and `db`.
When deploying the application, docker compose maps port 80 of the web service container to port 80 of the host as specified in the file.
Make sure port 80 on the host is not being used by another container, otherwise the port should be changed.

## Deploy with docker compose

```
$ docker compose up -d
 - Network alcides_default      Created                                                    0.1s
 - Container frontend           Started                                                    2.1s
 - Container alcides-mongo-1    Started                                                    1.9s
 - Container alcides-backend-1  Started                                                    2.4s
 - Container alcides-web-1      Starting                                                   2.5s

```

## Expected result

Listing containers must show three containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED       STATUS       PORTS                NAMES
2b21de09de39   nginx              "/docker-entrypoint.…"   5 hours ago   Up 5 hours   0.0.0.0:80->80/tcp   alcides-web-1
53286020d9ca   alcides-backend    "python3 src/server.…"   5 hours ago   Up 5 hours                        alcides-backend-1
5d1e6f597f72   mongo              "docker-entrypoint.s…"   5 hours ago   Up 5 hours   27017/tcp            alcides-mongo-1
eb676a8aacb8   alcides-frontend   "docker-entrypoint.s…"   5 hours ago   Up 5 hours                        frontend

```

After the application starts, navigate to `http://localhost:80` in your web browser:

Stop and remove the containers
```
$ docker compose down
```
