# Kubernetes

- Kubernetes is an open-source container orchestration platform developed by Google, released in 2014, and later donated to the CNCF (Cloud Native Computing Foundation).

- It automates the deployment, scaling, and management of containerized applications across a cluster of machines.

- The name Kubernetes comes from the Greek word meaning "helmsman" or "pilot" — the one who steers the ship. That's exactly what it does — steers your containers.

**K8s = K + 8 letters + s → shorthand used industry-wide.**

---

# Historical Evolution of Kubernetes

Before understanding Kubernetes, it's important to know how application deployment evolved over time.

---

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d7c7a7c2-5d6a-4747-804e-190d06e24ab9" />

---

## 1. Traditional Deployment Era

In the early days, applications were deployed directly on physical servers.

**Challenges:**

* Multiple applications shared the same server resources.
* One application could consume most of the CPU or memory.
* Other applications would experience poor performance.
* Running one application per server was expensive and led to resource wastage.

**Result:** Low resource utilization and high infrastructure costs.

---

## 2. Virtualization Era

To solve these issues, virtualization was introduced.

A physical server could now run multiple **Virtual Machines (VMs)**, each with its own operating system.

**Benefits:**

* Better resource utilization.
* Improved application isolation and security.
* Easier scaling and management.
* Reduced hardware costs.

**Limitation:**

Each VM contains a complete operating system, making it relatively heavy and consuming more resources.

---

## 3. Container Era

Containers were introduced as a lightweight alternative to virtual machines.

Unlike VMs, containers share the host operating system while keeping applications isolated.

**Benefits of Containers**


1. **Faster Deployment**

   * Quick application packaging and deployment.

2. **CI/CD Support**

   * Enables frequent releases and easy rollbacks.

3. **Consistency**

   * Same behavior across Dev, Test, and Production.

4. **Portability**

   * Runs on any cloud or operating system.

5. **Efficient Resource Usage**

   * Lightweight and uses fewer resources than VMs.

6. **Microservices Support**

   * Applications can be managed as independent services.

7. **Better Monitoring**

   * Easy tracking of application health, logs, and metrics.

---

# 4. Kubernetes Era (Container Orchestration)

- As organizations started running hundreds or thousands of containers, managing them manually became difficult.

- Kubernetes was introduced to automate container management and orchestration.
  
- What Kubernetes Does
  
  - Deploys applications automatically

  - Scales applications based on demand

  - Restarts failed containers (Self-Healing)

  - Distributes traffic using Load Balancing

  - Manages storage and networking

  - Ensures high availability of applications

---

### In Simple Terms

**Physical Servers → Virtual Machines → Containers → Kubernetes**

Kubernetes helps manage containers efficiently at scale, making modern cloud-native applications reliable, scalable, and easy to operate.

---

# Docker vs Kubernetes — What's the Difference?

**Docker**

- **Docker** is an open-source containerization platform that allows developers to package an application along with its dependencies, libraries, and configuration files into a lightweight, portable unit called a **container**, which can run consistently across any environment.

---

**Kubernetes**

- **Kubernetes (K8s)** is an open-source **container orchestration platform** originally developed by Google, that automates the deployment, scaling, load balancing, self-healing, and management of containerized applications across a cluster of nodes.

---

**Together**

- Docker **builds and runs** containers on a single host. 

- Kubernetes **orchestrates and manages** those containers across multiple hosts in a distributed environment, ensuring availability, scalability, and resilience.

---
