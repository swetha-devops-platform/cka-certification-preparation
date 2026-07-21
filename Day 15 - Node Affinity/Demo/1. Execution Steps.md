# Node Affinity - Required type example

Step 1: Writing Affinity.yml 

---

<img width="621" height="468" alt="image" src="https://github.com/user-attachments/assets/d978a351-7b85-4012-81c1-d138f5882d4c" />


---

Step 2 : Creating an Pod and it will be in Pending state beacuse our node is not labeled 

---

<img width="736" height="57" alt="image" src="https://github.com/user-attachments/assets/b7b28403-ecd2-426b-b6af-73685c9b1672" />

---

<img width="650" height="80" alt="image" src="https://github.com/user-attachments/assets/c2b4005a-7704-481a-ab79-a23b69ff83d3" />


Step 3: Labeling the node 

---

<img width="925" height="122" alt="image" src="https://github.com/user-attachments/assets/19b0c2e4-dbd8-481e-b57f-0acde0d0d317" />


---

Step 4: Checking the pod status 

---

<img width="586" height="83" alt="image" src="https://github.com/user-attachments/assets/54265265-ed26-405d-b2ab-4d7ce17ca2e6" />

---

# Node Affinity - Preference type 

Step 1 : Writing the Affinity2.yml

---

<img width="680" height="471" alt="image" src="https://github.com/user-attachments/assets/4a6e497e-474e-4780-98c1-381ac8f78cc7" />

---

Step 2: Creating the pod and checking whelther it is running or not 

---

<img width="801" height="197" alt="image" src="https://github.com/user-attachments/assets/fe4c3bfe-16b6-4bf1-970c-84bfbe8bbe03" />

---

# Node Affinity - Operator ( exists ) 

---

Step 1 : Changing the Operator as Exists 

---

<img width="628" height="464" alt="image" src="https://github.com/user-attachments/assets/c551033b-8465-4c6b-90d1-f98918cc4314" />


---

Step 2 : Changing the node lable as " environment="

---

<img width="954" height="61" alt="image" src="https://github.com/user-attachments/assets/4acc6f2a-4245-4ca6-ab29-78253d1e7adc" />


---

Step 3 : Applying the changes and checking whelther pod is running or not 

---

<img width="1201" height="250" alt="image" src="https://github.com/user-attachments/assets/e6ac4f49-d678-4bab-9810-0a7dc3e092ea" />


---
