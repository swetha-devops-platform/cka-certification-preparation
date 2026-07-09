# Kubernetes Terminology

1. **Pod** – The smallest deployable unit in Kubernetes; wraps one or more containers.
2. **Node** – A machine (VM or physical) where pods are scheduled and run.
3. **Cluster** – A set of nodes managed by a control plane.
4. **Deployment** – Manages rolling updates and ensures desired number of pod replicas.
5. **ReplicaSet** – Ensures a specified number of identical pods are running.
6. **StatefulSet** – Like Deployment, but for stateful apps with persistent identity and storage.
7. **DaemonSet** – Ensures a copy of a pod runs on all (or specific) nodes.
8. **Job** – Runs pods that complete a task and then exit.
9. **CronJob** – Schedules Jobs to run at specific times, like a cron task.
10. **Service** – Exposes a stable network interface to access pods.
11. **ClusterIP** – Default service type; accessible only within the cluster.
12. **NodePort** – Exposes the service on a static port across all cluster nodes.
13. **LoadBalancer** – Exposes the service externally using a cloud provider's load balancer.
14. **Ingress** – Manages external access to services via HTTP(S) with routing rules.
15. **ConfigMap** – Injects non-sensitive config data into pods as environment variables or files.
16. **Secret** – Like ConfigMap, but used for sensitive data like API keys or passwords.
17. **Volume** – Persistent storage attached to pods.
18. **PersistentVolume (PV)** – A piece of storage provisioned for the cluster.
19. **PersistentVolumeClaim (PVC)** – A request for storage by a pod.
20. **Namespace** – A way to divide cluster resources between multiple users or teams.
21. **Kubelet** – Agent running on each node that manages pod lifecycle.
22. **Kube-Proxy** – Manages network rules on nodes to forward traffic to correct pods.
23. **API Server** – Central control plane component that handles all API communication.
24. **Controller Manager** – Runs background controllers that enforce cluster desired state.
25. **Scheduler** – Assigns pods to available nodes based on resource requirements and constraints.

*(Note: item 25 "Scheduler" appeared twice in the original post — duplicate removed here.)*

Want me to turn this into a GitHub notes file too, since it'd pair well with your Day 07/08 pod notes as a quick-reference glossary?
