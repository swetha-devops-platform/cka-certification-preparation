# The Traditional Way 

---

<img width="789" height="363" alt="image" src="https://github.com/user-attachments/assets/bcf81927-e04d-419e-9cda-90d5e6089c0e" />


---

- The code passes in Dev — because the developer just wrote it and tested it locally.

- It passes again in Test — because that environment happens to be similar enough. So everyone assumes it's ready.

- Then it gets handed to Ops for the real deployment, and it fails in Production.

- Why?

  - Because Dev, Test, and Prod aren't identical.
  
  - Maybe Prod has different environment variables, due to misconfiguration and misalignments, a different OS version, library version, missing dependencies, or scaled-up traffic that exposes a bug the smaller test environment never hit.
  
  - The developer's classic (and slightly infamous) line at this point is: **"but it works on my machine."**

- This is exactly the problem **containers solve** — package the app with everything it needs (dependencies, config files , runtime, binaries, Aplication and OS) into one image, and that same image runs identically in Dev, Test, and Prod.

---

# The Modern Way 

---

<img width="791" height="370" alt="image" src="https://github.com/user-attachments/assets/09306707-e9d2-48f4-932a-a95a87dea52b" />

---

- Docker packages your app and everything it needs — the runtime, the libraries, the settings — into one sealed box called an **image.**

- That same box gets used in Dev, Test and Prod. It works all Three Stages because nothing is different between the stages.

- It's not three separate setups that hopefully match — it's literally one box, used three times.

- So there's **no more "it works on my machine."** and The developer just hands the box to Ops, Ops runs it, and it works.
  
**That's the goal of Container: build the app, ship it and run it anywhere, exactly the same every time.**

---

# Containers VS Virutal Machine 

---

<img width="735" height="333" alt="image" src="https://github.com/user-attachments/assets/40662792-975b-48f1-8cad-7c376920ae01" />

---

| Feature          | Container                                      | Virtual Machine                       |
| ---------------- | ---------------------------------------------- | ------------------------------------- |
| **Architecture** | Shares the host OS kernel                      | Has its own guest OS and kernel       |
| **Startup Time** | Starts in milliseconds                         | Takes seconds to minutes              |
| **Size**         | Usually MBs                                    | Usually GBs                           |
| **Performance**  | Near-native performance                        | Slight overhead due to the hypervisor |
| **Isolation**    | Process-level isolation (Namespaces & Cgroups) | Hardware-level isolation (Hypervisor) |

---

- Containers and virtual machines are both used for application isolation, but they work differently.

- The biggest difference is that containers share the host operating system kernel, whereas each virtual machine runs its own guest operating system and kernel.

- Containers start in milliseconds and are lightweight because they package only the application and its dependencies. Virtual machines take longer to boot and consume more resources because they include an entire operating system.

- Containers provide process-level isolation using Linux namespaces and cgroups, while virtual machines provide hardware-level isolation through a hypervisor.

- Due to their lightweight nature, containers offer near-native performance and allow much higher application density than virtual machines.

In modern production environments, we often run containers inside virtual machines to combine the strong isolation of VMs with the speed and efficiency of containers."

---

# Containers V/S Virtual machines - Example - a Building analogy

---

<img width="755" height="347" alt="image" src="https://github.com/user-attachments/assets/6726119f-b90b-4ac9-86f3-e7a5bdf67d29" />


---

**Containers = Apartment building**

- All units share the same building — the same operating system and infrastructure
- Each unit (container) still has its own space — its own app and dependencies, isolated from the others
- Fast and cheap to add a new unit, since the building already exists
- Downside: if something's wrong with the building itself (the shared OS/kernel), it can affect every unit in it

**Virtual Machine = Standalone house**

- Each house is built completely separately — its own foundation, its own full structure (Guest OS)
- Nothing is shared with any other house — fully independent from the ground up
- Slower and more resource-heavy to "build," since you're constructing the whole house every time
- Upside: total isolation — nothing happening in one house can ever touch another

**The one-line summary:**

- Containers → shared foundation, fast and light, isolated apps
- VMs → separate foundation, slower and heavier, isolated *everything*


---


# Docker 

- Docker is an open-source containerization platform that allows you to package an application along with all its dependencies — code, runtime, libraries, and configuration — into a single portable unit called a **container.**

- Isolated Environment that Contains Libraries, Application, runtime and Dependices

- Lightweight Sandbox Environment

---

# Simple Docker Flow : 

---

<img width="1691" height="930" alt="image" src="https://github.com/user-attachments/assets/fd31d8a4-7e73-4802-b4aa-3bca5a295d6e" />


---

- **Dockerfile** 

  - A Dockerfile is a plain text file that contains step-by-step instructions to build a Docker image.
  
  - Docker reads this file from top to bottom and executes each instruction as a layer.

- **Docker Images**

  - A Docker Image is a read-only template used to create containers.
  
  - This Images are shipable images which means we can ship this images from one environment to otherone but we cannot do it for Containers

- **Docker Registry**

  -  A Docker Registry is a storage and distribution system for Docker images — think of it exactly like GitHub, but instead of storing code, it stores container images

  - Docker Hub is the default public registry — it hosts millions of official images like Ubuntu, Nginx, Node, and Postgres that anyone can pull for free
 
- Docker Images wil be Converted into an Running Instances by using an Command of **Docker run**

---

# Docker Architecture 

---

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3c68390f-b63c-4af2-85eb-f096201992c3" />

---

- **Docker Client** — This is how you interact with Docker. Commands like `docker build`, `docker pull`, `docker run` are typed here, and they get sent to the Docker Daemon as instructions.

- **Docker Host** — The machine actually running Docker. Inside it lives the **Docker Daemon** called (dockerd), the background process that does all the real work: building images, starting containers, and managing everything on this host.

- **Images** — Read-only templates (like `ubuntu`, `redis`, `nginx`) that contain everything needed to run an app. Think of an image as a blueprint — you can't run it directly, but you can create containers from it.

- **Containers** — Running instances created from images A container is a lightweight, isolated runtime environment that packages an application along with all its dependencies, libraries, configuration files, and runtime. This allows the application to run consistently across different environments, such as a developer's laptop, a testing server, or production.

Unlike a virtual machine, a container does not include its own operating system. Instead, it shares the host operating system's kernel, making it much smaller, faster to start, and more resource-efficient.

Docker is the most commonly used container platform for creating, running, and managing containers.

- **Docker Registry** — A remote storage location for images (Docker Hub is the public one; companies also run **Private Registries**). You **pull** images down from here to run locally, and **push** images up here to share or deploy them elsewhere.

**The flow in one line:** You type a command (Client) → the Daemon on the Host executes it → it either pulls an Image from the Registry or runs a Container from an existing Image → and you can push new images back to the Registry to share them.


---

# Difference Between Docker Image & Containers 

A Docker image is a read-only template that contains the application code, runtime, libraries, dependencies, configuration files, and metadata required to run an application. It serves as the blueprint for creating containers.

A Docker container is a running instance of a Docker image. When a container is started, Docker adds a thin writable layer on top of the read-only image so the application can execute and make changes without modifying the original image. Multiple containers can be created from the same Docker image.

