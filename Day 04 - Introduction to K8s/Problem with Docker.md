# Problems with Docker (Why Kubernetes?)


# Use Case:1

- If the 1st container is consuming more memory, the **8th container will start to die** because Docker will take resources away from it.

- According to the **Linux kernel algorithm rules**, it will kill the process based on those rules. So before the 8th container even gets started, it is already being killed.

# Problem 1 — Single Host

- The nature of Docker as a container platform is scoped to a **single host**. Because of this, containers can impact each other.If one container is impacting another, there is no way to isolate them in Docker.

---

# Use Case:2

- Suppose someone kills the container that is hosting the application. Immediately, the app inside that container **will not be accessible to users**.

- Why? Because when the container is killed, unless a DevOps engineer manually restarts it, the application inside that killed container **will remain inaccessible**.

# Problem 2 — No Autohealing

- There are hundreds of reasons for containers to go down, and the problem is that **DevOps Engineers cannot monitor containers 24/7**.

- There could be **10,000 containers running in production** in a single organization.

- Autohealing is the behaviour where, **without any manual intervention from the user**, the container restarts itself automatically.

- Autohealing is the **most important concept** in container management.

---


# Use Case:3 — Netflix Scenario:

| | Resources |
|---|---|
| Container (Docker) | 4 GB RAM, 4 CPU |
| App inside container | Netflix — serving 10,000 users |

- During **festival seasons**, 10,000 users can spike to **1 lakh (100,000) users**. When the load increases, additional resources must be provisioned automatically to handle it.

- **There are 2 ways to scale:**

  - **Manually** — increase the number of containers from C1 to C10 by hand
  
  - **Automatically** — containers should scale up on their own based on load

- But **Docker does not support** either of these approaches natively. There should be a **load balancer** as part of an autoscaling setup — which Docker does not provide.

# Problem 3: No Autoscaling

- Docker has no built-in autoscaling or load balancing support.

---


# Use Case:4

- Docker is **minimalist and very simple by nature**.

- By default, Docker does not support **enterprise-level application requirements**. For enterprise-readiness, we need capabilities such as:

  - Load Balancer
    
  - Firewall
    
  - Autoscaling
    
  - Autohealing
    
  - API Gateway

# Problem 4 — No Enterprise-Level Support

These are **enterprise-level standards** — and Docker does not support them out of the box.

---

# Solution — Kubernetes

- These **4 problems are solved by Kubernetes**.
  
- There are around 100 problems with Docker at scale, but these **4 are the most important ones.**

```
Problem of Docker  →  Solution  →  Kubernetes  →  Container Orchestration Platform
```

