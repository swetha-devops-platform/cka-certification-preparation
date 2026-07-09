# Kubernetes architecture 

Kubernetes is split into two fundamental planes: the **Control Plane** (the brain) and the **Worker Nodes** (the muscle). 

Let's visualize it: Now let me walk you through each component:

---

## Architecture Overview

Kubernetes architecture is divided into two planes:

| Control Plane | Data Plane |
|---|---|
| API Server | kubelet |
| etcd | kube-proxy |
| Scheduler | Container Runtime |
| Controller Manager | |
| Cloud Controller Manager (CCM) | |

---


<img width="911" height="845" alt="image" src="https://github.com/user-attachments/assets/e8ad0ab2-2d57-4b59-a169-e5dde8f494ab" />


---


# Control Plane and Data Plane 

**Control Plane — What should happen?**

It makes **decisions** about the cluster. It doesn't run your application workloads.

| Component | Role |
|---|---|
| API Server | Gateway for all operations |
| etcd | Stores desired + actual state |
| Scheduler | Decides *which node* a pod goes to |
| Controller Manager | Reconciles actual state to desired state |

---

**Data Plane — Make it happen**

It **executes** the decisions made by the control plane. Your actual app containers run here.

| Component | Role |
|---|---|
| kubelet | Receives pod specs, starts containers |
| kube-proxy | Sets up networking/routing rules |
| Container Runtime | Actually runs the containers (containerd) |
| Pods | Your app workloads live here |


---

## The key separation

```
You (kubectl)
     ↓
Control Plane  →  "Pod X should run on Node 2 with 2 CPUs"
     ↓
Data Plane     →  kubelet pulls image, starts container, reports back
```

This separation is why Kubernetes is so resilient — even if the control plane goes down temporarily, the data plane keeps running existing pods. Your app stays up; you just can't make *new changes* until the control plane recovers.

---

| Feature                    | Control Plane (Master Node)                                                     | Data Plane (Worker Node)                              |
| -------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Role**                   | Decides what should happen in the cluster                                       | Executes the decisions made by the Control Plane      |
| **Runs On**                | Master Node                                                                     | Worker Nodes                                          |
| **Failure Impact**         | Cannot schedule new workloads or make cluster changes                           | Existing pods on other healthy nodes continue running |
| **Main Components**        | API Server, etcd, Scheduler, Controller Manager, Cloud Controller Manager (CCM) | Kubelet, kube-proxy, Container Runtime, Pods          |
| **Primary Responsibility** | Cluster management and orchestration                                            | Running application workloads                         |
| **Handles**                | Scheduling, desired state management, cluster configuration                     | Container execution, networking, and pod lifecycle    |
| **Stores Cluster State**   | Yes (via etcd)                                                                  | No                                                    |
| **Communicates With**      | All cluster components                                                          | Control Plane and Pods                                |
| **Example**                | Decides where a Pod should run                                                  | Actually runs the Pod on a node                       |

---

# Control Plane Components : 

**1. API Server**

  - The **core component** of Kubernetes

  - Responsible for **all incoming requests** and enforcing communication standards

  - K8s and external tools interact with the cluster **only through the API Server**

  - It will **decide the pod lifecycle** — where to create the pod and on which node

  - It is the **heart of Kubernetes** and handles requests from external sources too

---

**2. Scheduler**

  - Responsible for **scheduling pods** onto nodes

  - The API Server decides which node is available; the Scheduler **assigns pods to those nodes**

  - The component that is "scheduling pods to the node" is the **Scheduler**

  - picks the best node based on resource availability, taints, tolerations, and affinity rules.

---

**3. etcd**

  - **a distributed key-value datastore** that holds the *entire cluster state*.
  
  - Think of it as the source of truth. What pods exist, what namespaces, what configs — all in etcd

  - **Backs up** information about the Kubernetes cluster and its stores in document format(json or yaml).

  - The Kubernetes API Server is the gateway to the cluster and the only control plane component that directly reads from and writes to etcd.
  
  - All other components (Scheduler, Controller Manager, Kubelet, and kubectl) communicate with the API Server instead of accessing etcd directly.

---

**4. Controller Manager**

   - To Supports **Autoscalling**, we need an Controllers and to ensure whelther this controller is running or not we need an **Controller Manager**

   - runs a set of controllers in the background **(ReplicaSet controller, Deployment controller, Node controller, etc.)**.
   
   - Its job is to continuously reconcile *actual state* → *desired state* of the pods 
   
   - If a pod dies and you have a ReplicaSet of 3, the controller notices and creates a new one.

---

**5. Cloud Controller Manager (CCM)**

  - Ensures that replicas are running — needs a **Controller** and a **Controlled** mechanism

  - Cloud providers (e.g., AWS EKS) run Kubernetes **on cloud platforms** like EKS

  - When Kubernetes is on the cloud, it needs to understand cloud-specific resources like: Load Balancers and Storage

  - **Cloud providers need to understand the mechanism by which CCM is controlled**

**Example:** On AWS EKS, Kubernetes should integrate with cloud provider services. The Cloud Controller Manager is responsible for this.

---

# Data Plane Components (Worker Node)

**1. kubelet**

  - Called the **"Docker of K8s"** — it is the **node agent**

  - Responsible for **running a pod**, **creation of pods** and also for **managing pods**

  - Needs a **Container Runtime** to function

  - It watches the API server for pods assigned to its node and then tells the container runtime to start/stop containers.
  
  - It also reports node health back to the control plane.

---

**2. kube-proxy**

  - This component **manages the network** of the pod

  - handles networking rules on each node (using `iptables` or `ipvs`).
  
  - It enables the Service abstraction — so `curl my-service:8080` actually reaches the right pod IP.

  - Assigns **IP addresses**, manages **load balancing capability**, IP tables on the Linux side

  - **Net config** — responsible for managing networking rules on the node

---

**3. Container Runtime**

  - The actual engine that runs containers.
  
  - Kubernetes has an interface called the **Container Runtime Interface (CRI)** which supports multiple container runtimes, so it works with containerd, CRI-O, or others.

  - Dockershim was removed in Kubernetes v1.24. **containerd** and **CRI-O** are the recommended runtimes now.

| Runtime | Notes |
|---|---|
| **Docker** | Classic option |
| **Dockershim** | Built-in Kubernetes shim (deprecated) |
| **containerd** | Most widely used today |
| **CRI-O** | Lightweight, Kubernetes-native |

---

**4. Pods** 

  - the smallest deployable unit.

  - Example : Baby in womb 
  
  - A pod wraps one or more containers that share network (same IP) and storage.
  
  - Usually one container per pod, unless you're using the sidecar pattern (like Istio envoy proxy or a log shipper).

---

## Kubernetes Workflow ( Pod Creation )

1. **User** (a DevOps engineer or Kubernetes admin) runs a command using `kubectl` to create a pod.
2. **kubectl** is the CLI client that communicates with the control plane. It sends the pod creation request to the API server.
3. **API server** authenticates and validates the incoming request.
4. **Etcd** — the API server doesn't create the pod itself. Instead, it writes an entry into etcd (the cluster's key-value store) representing the desired pod state.
5. Etcd confirms back to the **API server** that the entry has been created.
6. **Scheduler** watches the API server for pods with no assigned node. It selects a suitable node and sends this scheduling decision back to the API server.
7. **API server** authenticates, validates, and updates etcd with the scheduling decision, then forwards the pod spec to the kubelet on the chosen node.
8. **Kubelet** receives the instruction, creates the pod on that node, and reports back to the API server that the pod is running.
9. **API server** updates etcd with the final pod status.
10. **User** sees the pod created successfully — this confirmation comes from the API server.

---

<img width="1980" height="2640" alt="image" src="https://github.com/user-attachments/assets/ef0f7344-1b17-4a81-b904-4b93dabc87c6" />


---
