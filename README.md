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

Issue: Upon the initial push to GitHub, a warning was generated indicating a file size exceeding 50MB (the Terraform Helm provider binary).
Resolution: Realized that the .terraform directory was accidentally committed. Created a .gitignore file to exclude .terraform/, .tfstate, and .tfvars files, then used git rm -r --cached .terraform to untrack the directory without deleting it locally.

## 🔄 GitOps Continuous Delivery (ArgoCD)
To achieve a true GitOps workflow, I deployed ArgoCD to the Kubernetes cluster. 
1. ArgoCD was configured to monitor the `helm-chart` directory in this GitHub repository.
2. Automatic Sync and Self-Heal policies were enabled. 
3. **Result:** Any manual changes made to the cluster (e.g., deleting a pod) are automatically reverted by ArgoCD to match the desired state defined in Git.

**Troubleshooting Note:** During initial setup, ArgoCD failed to sync due to a namespace case-sensitivity error (`namespaces "Default" not found`). I resolved this by updating the destination namespace in the ArgoCD Application manifest to lowercase (`default`).
