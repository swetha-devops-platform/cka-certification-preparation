# Pods in Kubernetes

A **pod** is the smallest deployable unit in Kubernetes — it's a wrapper around one or more containers that need to run together as a single unit.

**Key points:**

- A pod usually runs **one container**, but can run multiple containers that need to share resources tightly (like a main app + a logging sidecar).
- Containers inside the same pod share:
  - The same **network namespace** (same IP address, same localhost — they can talk to each other via `localhost`)
  - The same **storage volumes** (if defined)
- Pods are **ephemeral** — if a pod dies, Kubernetes doesn't repair it, it replaces it with a brand new pod (with a new IP). This is why you rarely talk to pods directly in production — you go through a Service instead.
- You never deploy a container directly in Kubernetes — you always deploy it wrapped inside a pod, even if it's just one container.

**Why not just run containers directly?**
Because Kubernetes needs a unit that can hold shared context — network, storage, lifecycle — for containers that are meant to work as a team. The pod is that unit.

---

## Two ways of creating pods

| | Imperative | Declarative (mostly used) |
|---|---|---|
| **How** | Direct `kubectl` commands | Configuration files (YAML or JSON) |
| **How it works** | You tell Kubernetes exactly what to do, one command at a time | You define the *desired state* of the object in a file, then apply it |
| **Used for** | Troubleshooting, quick one-off tasks | Production environments, CI/CD, GitOps |
| **Production ready?** | No | Yes |

**Why declarative wins for production:** 

- A YAML file can be re-applied any number of times and Kubernetes reconciles the cluster toward that state (idempotent).

- Imperative commands don't carry that memory — running the same `kubectl run` twice just throws an error instead of reconciling.

- This idempotency is exactly why GitOps tools like ArgoCD are built around declarative config.

---

## Example: creating an nginx pod (imperative)

```bash
kubectl run nginx-pod --image=nginx:latest
```

This creates a pod named `nginx-pod`.

```bash
kubectl get pods
```

```
NAME        READY   STATUS    RESTARTS   AGE
nginx-pod   1/1     Running   0          5s
```

`READY 1/1` means 1 out of 1 containers inside the pod is running.

---
