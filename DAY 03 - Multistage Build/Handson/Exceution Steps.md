# Docker Image Size Comparison: With vs Without Multi-Stage Build

A hands-on guide to understanding how multi-stage builds reduce Docker image size using a Python Calculator app.

---

# Steps to be followed: 

---

**Step 1: Launch an EC2 Instance**

  1. Go to **AWS Console → EC2 → Launch Instance**
  2. Choose **Ubuntu Server 22.04 LTS (Free Tier eligible)**
  3. Select instance type: `t2.micro` (Free Tier)
  4. Create or select an existing **Key Pair** (`.pem` file)
  5. Click **Launch Instance**

---

<img width="1920" height="349" alt="image" src="https://github.com/user-attachments/assets/4d6f75a2-9b42-4689-9462-767a13de08dd" />


---

**Step 2: Connect to EC2 via SSH**

---

<img width="996" height="656" alt="image" src="https://github.com/user-attachments/assets/a08befd7-35e3-4f1e-82a1-dc033bb2fa64" />


---



**Step 3: Install Docker on EC2**

---

<img width="578" height="65" alt="image" src="https://github.com/user-attachments/assets/d57b617a-ee6b-49bf-95fc-6c5d93c9615d" />


---

**Step 4: Clone Your GitHub Repository**

  - Install git on EC2 Instances - **sudo apt-get install -y git**
    
---

<img width="1417" height="196" alt="image" src="https://github.com/user-attachments/assets/6c2b1af6-e276-4aef-94bf-34e0bab9eb9a" />

---

**Step 5: Build the Docker Image**

**without multistage Dockerfile**

---

<img width="1010" height="608" alt="image" src="https://github.com/user-attachments/assets/817e5644-879a-48d9-bcef-9040c4689ece" />


---

**with multistage Dockerfile**

---

<img width="1128" height="30" alt="image" src="https://github.com/user-attachments/assets/4bea9c37-9ff6-4a77-bce9-ae4b16b91f84" />

<img width="835" height="48" alt="image" src="https://github.com/user-attachments/assets/dda66ee6-34ff-479f-8893-e0f777e9345c" />


---

**Expected Output:**

---

<img width="1039" height="174" alt="image" src="https://github.com/user-attachments/assets/4838a27d-66eb-4fea-835b-27ccf88f7567" />


---


## Size Comparison Summary

| Type                  | Base Image         | Includes          | Approx Size |
|-----------------------|--------------------|-------------------|-------------|
| Without Multi-Stage | `ubuntu:22.04`     | OS + build tools  |  156MB   |
| With Multi-Stage    | `python:3.11-slim` | Runtime only      |  45.5MB    |
| Size Reduction      | —                  | —                 |  70.8% smaller        |

---

## How Multi-Stage Build Works

---

```
┌─────────────────────────────────────────────────┐
│              WITHOUT Multi-Stage                 │
│                                                  │
│  ubuntu:22.04 + python3 + build-essential + app  │
│  Everything stays in the final image → LARGE     │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│               WITH Multi-Stage                   │
│                                                  │
│  Stage 1 (Builder)         Stage 2 (Final)       │
│  ubuntu + build tools  →   python:slim + app     │
│  (discarded)               only app copied →SMALL│
└─────────────────────────────────────────────────┘
```

---
