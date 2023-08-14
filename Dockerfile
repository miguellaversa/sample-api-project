FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set the working directory
WORKDIR /app

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client

# Copy the requirements file and install dependencies
COPY /api/requirements.txt .
RUN pip install -r requirements.txt

# Copy the API files to the working directory
COPY . /app

# Run the API
CMD ["python", "api/main.py"]