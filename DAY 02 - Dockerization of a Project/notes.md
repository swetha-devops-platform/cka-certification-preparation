# Dockerization of a Simple Python App 


**Step 1 : Create an Project Folder** 

Command : mkdir Dockerfile 

---

**Step 2 : Write your First Dockerfile** 

---

**Step 3 : Write Requirements.txt & myapp.py**

---


**Step 4 : Building an Docker Images by using below command**

  - **docker build . -t imagename** - . is for telling the docker to use all files in my machines 

---

<img width="1305" height="262" alt="image" src="https://github.com/user-attachments/assets/167aa3d1-b7b5-448a-91ce-956507290ee4" />

---

# Pushing docker images to DockerHub 

**Step 5 : Login into DockerHub**

---

<img width="1223" height="316" alt="image" src="https://github.com/user-attachments/assets/60331dc9-7c52-4cbf-b108-36384a67d81a" />

---

**Step 6 : Tagging the images - docker tag <local-image-name>:<tag> <dockerhub-username>/<repository-name>:<tag>**

  - **docker tag pyimage:latest swetha862001/pyimage:latest**

---

<img width="1248" height="53" alt="image" src="https://github.com/user-attachments/assets/4515e517-ca24-4c14-abbf-2af0cba4eb50" />

---

**Step 7 : Push the images to the Docker Hub**

   - **docker push swetha862001/pyimage:latest**

---

<img width="1330" height="269" alt="image" src="https://github.com/user-attachments/assets/71614bbd-adfe-42a6-9d7d-d807dd710a20" />


---

**Step 8 : Verify on Docker Hub**

---

<img width="1908" height="498" alt="image" src="https://github.com/user-attachments/assets/33355938-2d27-4541-b7cb-e77c2b480d41" />

---

**Step 9 : Run the Docker Images by using below command**

  - **docker run -it pyimages

---

<img width="793" height="55" alt="image" src="https://github.com/user-attachments/assets/6f121b1b-79ed-40e1-9cb4-a72391d00a32" />

---
