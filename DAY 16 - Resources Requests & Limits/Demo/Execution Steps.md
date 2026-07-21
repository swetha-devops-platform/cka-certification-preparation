# Resources requests and Limits 

Before Metric Server is not enabled 

---

<img width="627" height="54" alt="image" src="https://github.com/user-attachments/assets/57cbf4d1-2eb0-4a97-adcf-f1a09fd63817" />

---

Step 1 : Enabling Mertic Server 

  - minikube addons enable metrics-server

  - kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

---

<img width="1625" height="373" alt="image" src="https://github.com/user-attachments/assets/403fce08-57e7-4b0b-bcfe-6557edd30e6e" />

---

Step 2 : Checking metric Server is having an pod in Control plane components

---

<img width="1226" height="274" alt="image" src="https://github.com/user-attachments/assets/99108367-7910-4557-a34b-39a494dd3fc0" />

---

Step 3 : Checking CPU & MEM Utilization of node

---

<img width="685" height="79" alt="image" src="https://github.com/user-attachments/assets/b3789078-a3c5-40c6-a851-6e0f69e92443" />


---

# Task 1 : Memory Utilization demo

Notes: 

- Polinux/stress - This is espically builed to test the stress based on the arugments we are providing

Step 1 : Creating an namespaces and Creating pod and resources in that namespace 

---

<img width="714" height="58" alt="image" src="https://github.com/user-attachments/assets/28592d80-be5e-42e4-9040-4b1502ef943d" />


---

Step 2 : Creating an Yaml File - Memory.yml

---

<img width="808" height="429" alt="image" src="https://github.com/user-attachments/assets/a97af4df-68e0-49c4-9ff4-175ea136bb5e" />


---

Step 3 : Applying the Changes 

---

<img width="789" height="57" alt="image" src="https://github.com/user-attachments/assets/84c61dc5-1ab3-4a2d-805a-4d317a937274" />


---

Step 4 : Checking the Pod Status 

---

<img width="690" height="80" alt="image" src="https://github.com/user-attachments/assets/87c64b42-d0b2-4060-82f6-fc75a6612466" />

---

Step 5 : Checking Memory Utilization of the pod 

---

<img width="836" height="80" alt="image" src="https://github.com/user-attachments/assets/91f06bb2-845c-4dba-91b4-3fa6f2c7cba3" />

---

# Performing the Error 

Step 1 : Change the arguments value to 200m 

---

<img width="768" height="395" alt="image" src="https://github.com/user-attachments/assets/3945e9bc-e4a0-4f60-8025-26cedef78d6e" />

---

Follow the steps 2 to step 4 as mentioned above 

---

Checking memory utilization of the pod 

---

<img width="803" height="133" alt="image" src="https://github.com/user-attachments/assets/1c1b233e-f89e-46cf-8dfb-baa1bc8e1550" />


---
