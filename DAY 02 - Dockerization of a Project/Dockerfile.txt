# Step 1 - Base Image
FROM python:3.9-slim

# Step 2 - Set Working Directory
WORKDIR /app

# Step 3 - Copy Requirements File
COPY requirements.txt .

# Step 4 - Install Dependencies
RUN pip install -r requirements.txt

# Step 5 - Copy Application Code
COPY . .

# Step 6 - Expose Port
EXPOSE 8000

# Step 7 - Run the Application
CMD ["python", "myapp.py"]
