# without Configmaps & Secrets

---

Step 1: Create a pod without Configmaps

---

<img width="880" height="379" alt="image" src="https://github.com/user-attachments/assets/c996ca06-5b93-48e2-afd4-c3435a9f9b9a" />


---

<img width="661" height="60" alt="image" src="https://github.com/user-attachments/assets/e9e28f2f-3537-4645-869b-dc467593eccf" />


---

Step 2: Login into pod 

---

<img width="740" height="57" alt="image" src="https://github.com/user-attachments/assets/142af58a-98c3-438d-ad48-db956ed01c76" />


---

Step 3 : List the env variable 

---

<img width="520" height="84" alt="image" src="https://github.com/user-attachments/assets/0b557a0a-619f-4dda-acbc-2ed80c23609b" />

---

# With Configmaps - Imperative way 

---

<img width="1529" height="62" alt="image" src="https://github.com/user-attachments/assets/cac4398a-5fa9-48fb-b339-ac8967bec999" />

---

<img width="573" height="106" alt="image" src="https://github.com/user-attachments/assets/ddb04b3d-9c25-4a8e-ae57-41034d6c00e2" />

---

<img width="946" height="511" alt="image" src="https://github.com/user-attachments/assets/b7e42ce9-1690-415e-8f92-229e92bb4fc5" />


----

Esay method and followable - kubectl create cm myapp -from-file=app.config

---

# Decelartive way 

---

dry run it with -o yaml > cm.yml 

---


