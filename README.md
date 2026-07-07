# CKA Certification Prep — #40DaysOfKubernetes 

**Status: In Progress** — Day 1 of 40

My hands-on journey toward the **Certified Kubernetes Administrator (CKA)** certification, following the **#40DaysOfKubernetes** challenge structure by [Piyush Sachdeva](https://github.com/piyushsachdeva/CKA-2024). This repo documents my own notes, labs, and troubleshooting experience as I work through each day — built and verified on my own multi-cluster Minikube setup.

---

# About

- This repo is my personal learning log for the CKA exam, structured day-by-day (Docker fundamentals → Kubernetes core concepts → security → networking → troubleshooting → mock exam prep). 

- While I'm following the daily curriculum and topic order from Piyush Sachdeva's CKA-2024 YouTube series, all notes, commands, and lab exercises here are written and executed by me in my own environment.


# Credit 

- Course structure and daily topics based on [piyushsachdeva/CKA-2024](https://github.com/piyushsachdeva/CKA-2024). 

- If you're following the same challenge, that repo (and the accompanying [YouTube series](https://youtube.com/@techtutorialswithpiyush)) is the original source — go star it. 

---

# My Environment

Unlike the original course (which uses Kind), I'm practicing on:

- **Cluster:** Minikube — 3-context multi-cluster setup on WSL2
- **Practice Platforms:** [Killer.sh](https://killer.sh) (official simulator) & [KillerCoda](https://killercoda.com)
- **Tools:** kubectl, etcdctl, containerd, Helm

---

# Repo Structure

```
cka-certification-prep/
├── Day01-Docker-Fundamentals/
├── Day02-Dockerize-an-Application/
├── Day03-Docker-Multi-Stage-Builds/
├── Day04-Why-Kubernetes/
├── Day05-Kubernetes-Architecture/
├── ...
├── Day40-JSONPath-Advanced-kubectl/
├── Day41-Mission-CKA/
├── practice-exams/          # Killer.sh & KillerCoda scenarios
└── README.md
```

Each `DayXX` folder contains:
- `notes.md` — concepts explained in my own words
- `commands.md` / `manifests/` — YAML and CLI commands I ran
- `troubleshooting.md` — issues I hit and how I debugged them

---

# Progress Tracker

| Day(s) | Topic | Status |
|---|---|---|
| 1–3 | Docker Fundamentals & Multi-Stage Builds | In Progress |
| 4–6 | Why Kubernetes, Architecture, Local Cluster Setup |  Not Started |
| 7–17 | Pods, Deployments, Services, Namespaces, Scheduling, Autoscaling |  Not Started |
| 18–26 | Probes, ConfigMaps/Secrets, TLS, RBAC, Service Accounts, Network Policies |  Not Started |
| 27–32 | Kubeadm Cluster Setup, Storage, DNS, Networking | Not Started |
| 33–40 | Ingress, Upgrades, etcd Backup/Restore, Monitoring, Troubleshooting, JSONPath |  Not Started |
| 41 | Mission CKA — Exam Strategy & Final Revision |  Not Started |
| 42–46 | Real-time Projects (Container Registry, Helm, Kustomize, StatefulSets) |  Not Started |

*(Updated as I complete each day.)*

---

# Connect

- **LinkedIn:** [linkedin.com/in/swetha-ravi-717957215](https://linkedin.com/in/swetha-ravi-717957215)
- **GitHub:** [github.com/swetha-devops-platform](https://github.com/swetha-devops-platform)

---

*Following #40DaysOfKubernetes. Updated regularly as I progress — feedback and suggestions always welcome!*
