# Flask Prod App

This repository contains a simple Flask application that returns "Hello, DevOps!" on its root route as part of a DevOps challenge involving the lifecycle of an application. This document provides instructions on how to run the application, build its Docker image, deploy it on Kubernetes, and set up CI/CD pipelines.

## Prerequisites

- Python 3.12
- Docker
- Minikube or any Kubernetes distribution
- kubectl
- Docker Hub account (or other Docker registry)
- GitHub Account

## Running the Application Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/flask-prod-app.git
   cd flask-prod-app
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

   Access the application at `http://localhost:5000`.

## Building the Docker Image

1. **Build the Image**
   ```bash
   docker build -t your-dockerhub-username/flask-prod-app:latest .
   ```

2. **Run the Container Locally** (Optional)
   ```bash
   docker run -p 5000:5000 your-dockerhub-username/flask-prod-app:latest
   ```

## Deploying the Application on Kubernetes

1. **Start Minikube** (if using Minikube)
   ```bash
   minikube start
   ```

2. **Deploy the Manifest to Kubernetes**
   ```bash
   kubectl apply -f kubernetes/
   ```

3. **Check the Deployment Status**
   ```bash
   kubectl rollout status deployment/flask-prod-app-deployment
   ```

4. **Access the Application** (if using Minikube)
   ```bash
   minikube service flask-prod-app-service
   ```

## Setting Up the CI/CD Pipeline in GitHub Actions

1. **Create a Workflow File**
   - Go to `.github/workflows` and create a file named `ci.yaml` and `cd.yaml`.
   - Configure them as needed (see the example in the codebase).

2. **Configure GitHub Secrets**
   - Go to `Settings` > `Secrets` in your GitHub repository and add `DOCKER_USERNAME` and `DOCKER_PASSWORD` as your credentials for Docker Hub.

3. **Check the tab Actions**
   - Go to `Actions` in your GitHub repository and you can see triggered workflows, you can trigger then by creating a Pull request to a live environment or pushing code to a Live environment branch like `production`.
