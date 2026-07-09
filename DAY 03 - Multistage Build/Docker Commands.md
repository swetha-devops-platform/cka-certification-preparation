| **Purpose**                              | **Command**                                                      |
| ---------------------------------------- | ---------------------------------------------------------------- |
| Build the Docker image                   | `docker build -t todoapp-docker .`                               |
| List all Docker images                   | `docker images`                                                  |
| Login to Docker Hub                      | `docker login`                                                   |
| Tag the Docker image                     | `docker tag todoapp-docker:latest username/new-reponame:tagname` |
| Push the image to Docker Hub             | `docker push username/new-reponame:tagname`                      |
| Pull the image from Docker Hub           | `docker pull username/new-reponame:tagname`                      |
| Run the Docker container (Detached Mode) | `docker run -dp 3000:80 username/new-reponame:tagname`           |
| List running containers                  | `docker ps`                                                      |
| List all containers (Running + Stopped)  | `docker ps -a`                                                   |
| Access the running container             | `docker exec -it <container-name> sh`                            |
| View container logs                      | `docker logs <container-name>`                                   |
| Inspect container details or Config details              | `docker inspect <container-name>`                                |
| Stop a running container                 | `docker stop <container-name>`                                   |
| Start a stopped container                | `docker start <container-name>`                                  |
| Restart a container                      | `docker restart <container-name>`                                |
| Remove a stopped container               | `docker rm <container-name>`                                     |
| Remove a Docker image                    | `docker image rm <image-id>`                                     |
| Remove unused Docker resources           | `docker system prune`                                            |
| View Docker version                      | `docker --version`                                               |
| View Docker system information           | `docker info`                                                    |
