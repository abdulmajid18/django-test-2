# Set the base image
FROM python:3.11.4-slim-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY k8-nginx .

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
