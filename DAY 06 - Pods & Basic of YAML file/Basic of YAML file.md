# Day 08: YAML basics and creating pods declaratively

## Basics of a YAML file

- File extension: `.yml` or `.yaml`
- Used for configuration — it's how we describe the *desired state* of
  Kubernetes objects.
- YAML supports different data types: strings, integers, lists, and
  dictionaries (maps).
  
- YAML is indentation-sensitive because indentation defines the hierarchy and relationship between fields.

- Kubernetes uses this structure to understand the resource configuration. 

- If the indentation is incorrect, Kubernetes cannot parse the YAML correctly, resulting in a syntax or validation error, and the resource will not be created. 

- Therefore, we should always use spaces (typically two spaces per level) and never tabs.



### Dictionaries (key-value pairs)

A dictionary is just a set of fields nested under a key.

```yaml
Employee:
  name:
  age:
  address:
```

### Lists

Use a `-` to define list items. A list item can itself contain a sub-list.

```yaml
Employee:
  - name:
    age:
    address:
      - oldaddress
      - newaddress
```

---

## A pod YAML file, from the Kubernetes perspective

- YAML files in Kubernetes are **case-sensitive** — `apiVersion` is not the same as `APIVERSION`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    env: demo
    type: frontend
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
```

**The four required top-level fields for any Kubernetes object:**

| Field | Purpose |
|---|---|
| `apiVersion` | specifies which version of the Kubernetes API should be used to create and manage the object. |
| `kind` | The type of object — Pod, Deployment, Service, etc. |
| `metadata` | Data that identifies the object — name, labels, annotations |
| `spec` | The desired state — for a pod, this is the containers it should run |

**Not sure which apiVersion to use?**
```bash
kubectl explain pod
```
This tells you the correct `apiVersion` and walks you through every field a Pod spec supports.

```bash
kubectl explain pod --recursive
```
Shows the *entire* nested field tree at once — useful once you already know roughly what you're looking for.

---

## Working with the pod YAML file

```bash
kubectl create -f pod.yaml     # create the object from file
kubectl delete pod <name>      # delete the pod
```

**For troubleshooting:**

```bash
kubectl describe pod <name>    # full details: events, status, restarts
kubectl edit pod <name>        # opens the live object in an editor —
                                # changes apply immediately, no separate
                                # apply step needed
kubectl exec -it <podname> -- sh   # open an interactive shell inside
                                    # the pod's container
```

- **Worth adding:** `kubectl create -f` fails if the object already exists.
- `kubectl apply -f` is idempotent — it creates the object if it doesn't exist, and updates it if it does. This is why `apply` is the one used in real pipelines and GitOps, not `create`.

---

## Turning imperative commands into a declarative YAML file

You can generate a YAML template from an imperative command instead of writing it by hand — useful for scaffolding and troubleshooting.

```bash
# Generates the YAML AND actually creates the pod
kubectl run nginx --image=nginx -o yaml > pod.yaml
```

- **Correction/addition:** the command above still *creates the pod* — the `-o yaml` just also prints the YAML. 

- If you only want the file, without creating anything in the cluster, add `--dry-run=client`:

```bash
# Generates the YAML WITHOUT creating anything in the cluster
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
```

This is the standard trick for spinning up a starting template for a new pod, then editing the fields you need (name, image, labels) before applying.

---

## More useful commands

```bash
kubectl describe pod <podname>              # full details about a pod
kubectl get pods <podname> --show-labels    # see the pod's labels
kubectl get pods -o wide                    # full details incl. node, IP
kubectl get nodes                           # list nodes
kubectl get nodes -o wide                   # list nodes with more detail
                                             # (IP, OS, kubelet version)
```

---

## Summary

- A Kubernetes YAML manifest always needs four things — apiVersion, kind, metadata, and spec.

- I can hand-write it or scaffold it fast using `kubectl run ... --dry-run=client -o yaml`, which gives me a valid template without actually touching the cluster.

- In production I always use `apply`, not `create`, because apply is idempotent and that's what makes GitOps workflows possible.

