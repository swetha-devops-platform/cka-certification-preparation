# Docker Multi-Stage Builds


**Multi-Stage Build**

- Multi-Stage Build in Docker is a technique used to create lightweight and optimized Docker images. 

- In this approach, we use multiple stages inside a single Dockerfile. 

- The first stage is usually used for building the application and installing all dependencies, while the final stage contains only the required runtime files. 

- This helps reduce image size, improves security, and makes the container more efficient for production environments

- Example: 
  
```
# Stage 1 — Build
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Stage 2 — Production (only takes what it needs)
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```
---

## Why Multi-Stage Builds?

**The Problem (Single Stage):**

- We use a base image like Ubuntu, but it comes with many unnecessary packages, dependencies, and tools. In most cases, we only need a Python runtime to run the application.

- To solve this problem, Docker introduced the concept of Multi-Stage Builds. 

- Multi-stage builds help reduce the size of the Docker image by separating the build environment from the runtime environment. 

- Only the required files and dependencies are copied to the final image, making it lightweight, secure, and optimized for production use.

```
Single Stage Image contains:
  ├── Node.js runtime (500MB)
  ├── npm (100MB)
  ├── All dev dependencies (300MB)
  ├── Source code
  ├── Test files
  ├── Build tools
  └── Compiled output (all you actually need!)

Total size: ~1GB 
```

**The Solution (Multi-Stage):**

```
Final Image contains:
  └── Compiled output only (served by nginx:alpine)

Total size: ~25MB 
```

---

# Benefits:

| Benefit | Description |
|---------|-------------|
| **Smaller images** | Only production artifacts in final image |
| **More secure** | No build tools, compilers, or source code exposed |
| **Faster deploys** | Smaller image = faster pull & start |
| **Cleaner** | One Dockerfile for entire build pipeline |
| **Cost saving** | Less storage, less bandwidth |
| **No secrets leak** | Build-time secrets don't end up in final image |

---

## How Multi-Stage Build Works

- Internally, Docker creates multiple intermediate images for each stage. 

- Using the COPY --from command, artifacts are copied from one stage to another. 

- Only the final stage becomes the production image, while intermediate stages are discarded unless explicitly retained.

```
Dockerfile with Multiple Stages:

┌─────────────────────────────────┐
│  Stage 1: builder               │
│  FROM node:18                   │
│  RUN npm install                │  ← Temp container
│  RUN npm run build              │  ← Discarded after build
│  Output: /app/dist              │
└──────────────┬──────────────────┘
               │
               │  COPY --from=builder /app/dist
               │  (only the compiled output)
               ▼
┌─────────────────────────────────┐
│  Stage 2: production            │
│  FROM nginx:alpine              │
│  COPY --from=builder ...        │  ← Final image
│                                 │  ← Only this is shipped!
└─────────────────────────────────┘
```

**Key Rules:**

- Each `FROM` starts a **new stage** with a **fresh filesystem**
- Previous stage files are **NOT automatically available**
- Use `COPY --from=stagename` to bring files across
- Only the **last stage** becomes the final image
- Intermediate stages are **discarded** (but cached!)

---

## Summary

```
SINGLE STAGE                    MULTI-STAGE
─────────────────               ──────────────────────────────
FROM node:18                    FROM node:18 AS builder
COPY . .                        COPY . .
RUN npm install                 RUN npm install && npm run build
RUN npm run build
CMD ["node", "dist/server.js"]  FROM node:18-alpine
                                COPY --from=builder /app/dist .
                                CMD ["node", "dist/server.js"]

Size: ~1.2 GB                   Size: ~120 MB
Security: Source exposed        Security: Source stays in builder
```

---
