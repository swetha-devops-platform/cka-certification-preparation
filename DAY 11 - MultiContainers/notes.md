# Init Containers and Sidecar Containers

**Interview summary line:** "Init containers run once, sequentially, before the app starts — they're for setup and gating. Sidecar containers run alongside the main container for the pod's whole life — they're for ongoing support like logging, proxying, or syncing data."

---

<img width="1775" height="894" alt="image" src="https://github.com/user-attachments/assets/9f8b945c-a4d0-4e89-873c-42c6ed4ecb1f" />

---

## 1. Init Containers

**What they are:** Special containers in a pod spec that run and complete **before** any app container starts.

**Key traits**
- Defined under `spec.initContainers`
- Run **sequentially**, one after another — container 2 doesn't start until container 1 exits `0`
- If an init container fails, kubelet restarts it (per pod `restartPolicy`) until it succeeds — the pod never reaches Running otherwise
- Can use a completely different image than the main container (e.g. a slim `busybox` for a setup task)
- Don't support `livenessProbe` / `readinessProbe` / `startupProbe` — they just need to exit successfully

**Common use cases**
- Wait for a dependency (DB, another service) to become available
- Pull config/secrets from an external source before app boot
- Run DB migrations
- Set correct file permissions on a mounted volume
- Clone a git repo into a shared volume for the main container to use

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  initContainers:
  - name: wait-for-db
    image: busybox:1.36
    command: ['sh', '-c', 'until nc -z db-service 5432; do echo waiting for db; sleep 2; done']
  containers:
  - name: myapp
    image: myapp:1.0
```

---

## 2. Sidecar Containers

**What they are:** Helper containers that run **alongside** the main app container for the pod's entire lifetime, sharing its network namespace and (optionally) its volumes.

**Key traits**
- Since **Kubernetes 1.29** (GA), native sidecars are defined as `initContainers` with `restartPolicy: Always` — Kubernetes then knows to start them first but keep them running like a normal container
- Before 1.29, "sidecar" was just a convention — a second entry under `spec.containers`, with no special ordering guarantees
- Share the pod's network (`localhost`) and can share mounted volumes with the main container
- Pod readiness waits on the sidecar too, so it doesn't get marked Ready before its helper is up

**Common use cases**
- Log shipping (e.g. Fluent Bit tailing app logs to a shared volume)
- Service mesh proxy (Istio/Envoy `istio-proxy`)
- Config/secret sync agents (e.g. `vault-agent`)
- Local metrics exporter sitting next to the app

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  initContainers:
  - name: log-shipper
    image: fluent-bit:2.2
    restartPolicy: Always        # <- this makes it a native sidecar
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
  containers:
  - name: myapp
    image: myapp:1.0
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
  volumes:
  - name: logs
    emptyDir: {}
```

---

## 3. Side-by-Side

| | Init Container | Sidecar Container |
|---|---|---|
| Runs | Before app starts | Alongside app, whole pod lifetime |
| Order | Sequential, one at a time | Concurrent with main container |
| Exits | Must exit `0` to proceed | Expected to keep running |
| Probes | Not supported | Supports liveness/readiness/startup |
| Spec location | `initContainers` | `initContainers` + `restartPolicy: Always` (1.29+) or plain `containers` (older) |
| Typical use | Setup, gating, migrations | Logging, proxying, syncing |

---


