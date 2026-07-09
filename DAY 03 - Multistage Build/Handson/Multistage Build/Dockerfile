# ─── Stage 1: Builder ───────────────────────────────
FROM ubuntu:22.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and build dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY myapp.py .

# ─── Stage 2: Final (lean runtime image) ────────────
FROM python:3.11-slim AS final

WORKDIR /app

# Copy only the app file from builder stage
COPY --from=builder /app/myapp.py .

CMD ["python3", "myapp.py"]
