# Kubernetes: How It Solves 4 Core Problems


<img width="1139" height="720" alt="image" src="https://github.com/user-attachments/assets/426b8323-5e88-41a5-861e-49e30e015413" />

---

## Problem 1: Cluster Architecture

**Problem:** How should containers be organized and managed across multiple machines?

**How K8s solves it:**

- Kubernetes groups nodes into a **cluster**.
  
- By default, a cluster is created when Kubernetes is installed on the **master node**.
  
- This allows us to treat many machines as a single platform.
  
- Kubernetes can be installed at:
  
  - **Development level** — single node (e.g., Minikube)
    
  - **Production/Enterprise level** — multi-node cluster

**How clusters solve the problem:**

- Clusters group nodes together.
  
- This allows a single host to handle workloads distributed across nodes.
  
- When an app in Node A fails, Kubernetes automatically places it on another node.

---

## Problem 2: Autoscaling

**Problem:** How do we handle sudden spikes in load (e.g., during a festival, sale event)?

**Manual way (without K8s):**  

Go to `ReplicaSet.yaml` or `deployment.yaml` and manually increase the replica count.

```yaml
spec:
  replicas: 10  # manually changed from 1 to 10
```

**How K8s solves it — HPA (Horizontal Pod Autoscaler):**

- Kubernetes supports **HPA → Horizontal Pod Autoscaler**.
  
- You define a **threshold** (e.g., 80% CPU load).
  
- If the load exceeds 80%, Kubernetes automatically **spins up new pods/containers**.

```
Load > 80% threshold
      ↓
HPA triggers
      ↓
Spin up additional containers automatically
```


**Key concept:** Everything in Kubernetes is managed via **YAML files**.

---

## Problem 3: Self-Healing

**Problem:** What happens when a container crashes or gets damaged?

**How K8s solves it:**

- Kubernetes **controls the damage** — and often prevents it *before* it happens.
  
- Most of the time, Kubernetes detects issues before the container is fully damaged.

**Flow:**

```
Container going down
        ↓
API Server receives alert:
"Container is going down"
        ↓
Kubernetes rolls out a new container (before 10 minutes)
```


- **Kubernetes terminology:** In Kubernetes, a **Container** is referred to as a **Pod**.

---

## Problem 4: Enterprise-Level Application Support

**Problem:** Docker is not suitable for production because it does not support enterprise-level standard parameters.

**How K8s solves it:**

- Kubernetes originated from **Google**.
  
- **Borg** was Google's internal tool — Kubernetes is effectively a modern, open version of it.
  
- Kubernetes is **not just an open-source tool** — it has enterprise-level **container orchestration platform** capabilities.

--- 

**CNCF:**

- Kubernetes is governed by **CNCF → Cloud Native Computing Foundation**.
  
- The goal of the CNCF community is to make Kubernetes even better.
  
- They are continuously solving these problems — though not 100% yet.

---


**Docker not used in production** - **Why**

Docker does not support enterprise-level standard parameters. Kubernetes, backed by CNCF and originating from Google's Borg system, provides enterprise-grade container orchestration.
