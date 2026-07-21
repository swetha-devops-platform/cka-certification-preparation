# Taints & Toleration.md 

Step 1: Checking the nodes 

---

<img width="731" height="103" alt="image" src="https://github.com/user-attachments/assets/9a2d5481-92cd-4a90-9295-c920ad9ac5b2" />


---

Step 2: Applying Taints on Two Nodes 

---

<img width="964" height="113" alt="image" src="https://github.com/user-attachments/assets/ee18aac6-9d7e-491d-80a3-b8052bc7f360" />

---

Step 3 : Creating an pod and checking whelther it is running or not 

---

<img width="848" height="133" alt="image" src="https://github.com/user-attachments/assets/1dda39ec-d2a3-4225-bf5b-c940add321a8" />

It is in pending state, because the pod doesn't have a toleration 

---

Step 4 : Adding the Toleration to the pod.yml file we can do it by imperative way or in decelerative way 

---

<img width="775" height="110" alt="image" src="https://github.com/user-attachments/assets/94f89d11-8264-4e47-9160-387c37d7a6a0" />

---

<img width="262" height="327" alt="image" src="https://github.com/user-attachments/assets/a8f51acd-0eed-408b-b9ba-3ea722f93b54" />

---

Step 5 : Checking Whelther it is running or not 

---

<img width="546" height="86" alt="image" src="https://github.com/user-attachments/assets/f4c53e00-93c2-4c1b-8d19-ef866a94a023" />


---

Step 6: Removing the taints and checking whelther it is creating an pod or not 

---

<img width="964" height="51" alt="image" src="https://github.com/user-attachments/assets/48e6f005-8678-44bf-8ac2-411beb9be6c9" />

---

<img width="603" height="107" alt="image" src="https://github.com/user-attachments/assets/cd0546bb-bd1f-4643-bcba-46ee60cb929f" />

---
