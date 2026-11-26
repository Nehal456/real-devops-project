cat << 'EOF' > README.md
# Project Phoenix: Infrastructure as Code (IaC) Deployment

## 📌 Project Overview
In modern DevOps environments, manually provisioning Kubernetes clusters and deploying applications leads to configuration drift, human error, and slow onboarding. 

**Project Phoenix** solves this by using **Terraform** to automate the entire lifecycle of a local Kubernetes cluster and deploying a containerized two-tier application (Python/Flask + PostgreSQL) using a custom **Helm** chart. The infrastructure is completely reproducible, version-controlled, and idempotent.

## 🏗️ Architecture
1. **Terraform** provisions a local Kubernetes cluster using the **Kind** (Kubernetes in Docker) provider.
2. **Terraform** connects to the newly created cluster using the **Helm** provider.
3. **Helm** deploys custom Kubernetes manifests for:
   - A PostgreSQL database (Stateful backend).
   - A Python Flask application (2 replicas for high availability).
4. **Docker** hosts the Kind cluster and pulls the application image from the GitHub Container Registry (GHCR).

## 🛠️ Tech Stack
- **Infrastructure as Code:** Terraform
- **Orchestration:** Kubernetes (Kind)
- **Package Manager:** Helm
- **Container Runtime:** Docker Desktop (WSL 2 Integration)
- **Application:** Python (Flask), PostgreSQL
- **OS Environment:** Ubuntu (WSL 2 on Windows)

## 📂 Repository Structure
```text
project-phoenik/
├── main.tf                 # Terraform configuration (Kind & Helm providers)
├── README.md               # Project documentation
└── helm-chart/             # Custom Helm chart
    ├── Chart.yaml          # Helm metadata
    └── templates/          # Kubernetes manifests
        ├── app.yaml        # Flask Deployment & Service
        └── db.yaml         # PostgreSQL Deployment & Service
