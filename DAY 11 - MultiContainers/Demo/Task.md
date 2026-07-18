# Creating an Multi Containers Pods 

Step 1: Create an Pod.yaml file 

---

<img width="1279" height="77" alt="image" src="https://github.com/user-attachments/assets/c917895d-2217-43d2-846f-5b683919a5e5" />

---

Step 2: Create an deployment.yaml file 

---

Kubectl create deploy ngnix --image ngnix --port 80 

---


Step 3: Create an Services to expose the app by using below command

---

kubectl expose deploy ngnix deploy --name my service --port 80 

---

Step 4: Apply the changes 
