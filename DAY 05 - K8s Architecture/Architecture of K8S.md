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

<svg width="1320" height="2320" viewBox="0 0 1320 2320" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
<title>Kubernetes pod creation workflow</title>
<desc>Flowchart showing pod creation from user through kubectl, API server, etcd, scheduler, kubelet, kube-proxy, back to user, plus the controller manager's continuous reconcile loop.</desc>

<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#888780" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="arrow-dash" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#B4B2A9" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<rect width="1320" height="2320" fill="#FFFFFF"/>

<!-- User 1 -->
<rect x="490" y="40" width="340" height="80" rx="10" fill="#F1EFE8" stroke="#B4B2A9" stroke-width="1.5"/>
<text x="660" y="90" text-anchor="middle" font-size="24" font-weight="700" fill="#2C2C2A">User</text>
<text x="880" y="90" font-size="18" fill="#444441">Runs a kubectl command</text>
<line x1="660" y1="120" x2="660" y2="180" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- kubectl -->
<rect x="490" y="180" width="340" height="90" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="1.5"/>
<text x="660" y="215" text-anchor="middle" font-size="24" font-weight="700" fill="#0C447C">kubectl</text>
<text x="660" y="245" text-anchor="middle" font-size="18" fill="#185FA5">CLI client</text>
<line x1="660" y1="270" x2="660" y2="330" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- API server 1 -->
<rect x="470" y="330" width="380" height="90" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="1.5"/>
<text x="660" y="365" text-anchor="middle" font-size="24" font-weight="700" fill="#26215C">API server</text>
<text x="660" y="395" text-anchor="middle" font-size="18" fill="#3C3489">Authenticates, validates</text>
<line x1="660" y1="420" x2="660" y2="480" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- etcd -->
<rect x="470" y="480" width="380" height="90" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="1.5"/>
<text x="660" y="515" text-anchor="middle" font-size="24" font-weight="700" fill="#04342C">etcd</text>
<text x="660" y="545" text-anchor="middle" font-size="18" fill="#0F6E56">Creates pod entry</text>
<line x1="660" y1="570" x2="660" y2="630" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- API server 2 -->
<rect x="470" y="630" width="380" height="90" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="1.5"/>
<text x="660" y="665" text-anchor="middle" font-size="24" font-weight="700" fill="#26215C">API server</text>
<text x="660" y="695" text-anchor="middle" font-size="18" fill="#3C3489">Notifies scheduler</text>
<line x1="660" y1="720" x2="660" y2="780" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- Scheduler -->
<rect x="470" y="780" width="380" height="90" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="1.5"/>
<text x="660" y="815" text-anchor="middle" font-size="24" font-weight="700" fill="#4A1B0C">Scheduler</text>
<text x="660" y="845" text-anchor="middle" font-size="18" fill="#993C1D">Selects a node</text>
<line x1="660" y1="870" x2="660" y2="930" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- API server 3 -->
<rect x="390" y="930" width="540" height="90" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="1.5"/>
<text x="660" y="965" text-anchor="middle" font-size="24" font-weight="700" fill="#26215C">API server</text>
<text x="660" y="995" text-anchor="middle" font-size="18" fill="#3C3489">Updates etcd, forwards to kubelet</text>
<line x1="660" y1="1020" x2="660" y2="1080" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- kubelet -->
<rect x="390" y="1080" width="540" height="90" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="1.5"/>
<text x="660" y="1115" text-anchor="middle" font-size="24" font-weight="700" fill="#0C447C">kubelet</text>
<text x="660" y="1145" text-anchor="middle" font-size="18" fill="#185FA5">Starts containers on the node</text>
<line x1="660" y1="1170" x2="660" y2="1230" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- kube-proxy -->
<rect x="390" y="1230" width="540" height="90" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="1.5"/>
<text x="660" y="1265" text-anchor="middle" font-size="24" font-weight="700" fill="#0C447C">kube-proxy</text>
<text x="660" y="1295" text-anchor="middle" font-size="18" fill="#185FA5">Sets up network rules for the pod</text>
<line x1="660" y1="1320" x2="660" y2="1380" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="890" y="1355" font-size="18" fill="#444441">Pod is reachable</text>

<!-- API server 4 -->
<rect x="390" y="1380" width="540" height="90" rx="10" fill="#EEEDFE" stroke="#7F77DD" stroke-width="1.5"/>
<text x="660" y="1415" text-anchor="middle" font-size="24" font-weight="700" fill="#26215C">API server</text>
<text x="660" y="1445" text-anchor="middle" font-size="18" fill="#3C3489">Updates etcd with final status</text>
<line x1="660" y1="1470" x2="660" y2="1530" stroke="#888780" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- User 2 -->
<rect x="470" y="1530" width="380" height="90" rx="10" fill="#F1EFE8" stroke="#B4B2A9" stroke-width="1.5"/>
<text x="660" y="1565" text-anchor="middle" font-size="24" font-weight="700" fill="#2C2C2A">User</text>
<text x="660" y="1595" text-anchor="middle" font-size="18" fill="#444441">Sees pod created</text>

<!-- Controller manager -->
<rect x="960" y="900" width="300" height="120" rx="10" fill="#FAEEDA" stroke="#EF9F27" stroke-width="1.5"/>
<text x="1110" y="945" text-anchor="middle" font-size="24" font-weight="700" fill="#412402">Controller</text>
<text x="1110" y="980" text-anchor="middle" font-size="20" fill="#854F0B">manager</text>

<path d="M960 960 C 900 960, 900 570, 850 570" fill="none" stroke="#B4B2A9" stroke-width="1.5" stroke-dasharray="6 6" marker-end="url(#arrow-dash)"/>
<path d="M960 980 C 900 980, 900 1170, 930 1170" fill="none" stroke="#B4B2A9" stroke-width="1.5" stroke-dasharray="6 6" marker-end="url(#arrow-dash)"/>

<text x="1110" y="1055" text-anchor="middle" font-size="18" fill="#444441">Watches etcd</text>
<text x="1110" y="1082" text-anchor="middle" font-size="18" fill="#444441">continuously.</text>
<text x="1110" y="1109" text-anchor="middle" font-size="18" fill="#444441">If a pod crashes,</text>
<text x="1110" y="1136" text-anchor="middle" font-size="18" fill="#444441">restarts it via kubelet.</text>

<!-- Notes box -->
<rect x="60" y="1680" width="1200" height="480" rx="14" fill="#FFFFFF" stroke="#D3D1C7" stroke-width="1.5"/>
<text x="100" y="1740" font-size="24" font-weight="700" fill="#2C2C2A">API server's role throughout</text>
<text x="100" y="1790" font-size="19" fill="#444441">- Authenticates every incoming request</text>
<text x="100" y="1830" font-size="19" fill="#444441">- Validates request format and permissions</text>
<text x="100" y="1870" font-size="19" fill="#444441">- Reads and writes cluster state in etcd</text>
<text x="100" y="1910" font-size="19" fill="#444441">- Relays requests between scheduler, kubelet, and client</text>
<text x="100" y="1950" font-size="19" fill="#444441">- Sole component that talks directly to etcd</text>
<text x="100" y="1990" font-size="19" fill="#444441">- Controller manager also watches through it, not etcd directly</text>
<text x="100" y="2030" font-size="19" fill="#444441">- Returns responses back to kubectl / user</text>

</svg>
