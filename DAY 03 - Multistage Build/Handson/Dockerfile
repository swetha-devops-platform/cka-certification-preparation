# Single stage — full Ubuntu base image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and build tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY calculator.py .

CMD ["python3", "myapp.py"]
