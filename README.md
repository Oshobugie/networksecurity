# 🛡️ End-to-End Network Security MLOps Pipeline

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3%20%7C%20ECR-232F3E?logo=amazon-aws&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white)

## 📌 Overview
This repository contains a fully automated, containerized MLOps pipeline designed to detect network security threats (phishing). It handles the complete machine learning lifecycle: extracting raw data from MongoDB Atlas, validating schemas, training a classification model, and deploying it as a REST API. The system features continuous integration and continuous deployment (CI/CD) using GitHub Actions and AWS.

## 🏗️ System Architecture & Data Flow

This system implements a robust experiment tracking workflow via MLflow and DagsHub alongside a container registry workflow utilizing AWS ECR and a self-hosted EC2 runner.

```mermaid
graph TD
    subgraph Data Pipeline
        A[(MongoDB Atlas)] -->|Raw Phishing Data| B[Data Ingestion]
        B --> C[Data Validation<br/>Schema Checks]
        C --> D[Data Transformation<br/>KNN Imputer]
        D --> E[Model Trainer<br/>Classification]
    end
    
    subgraph Tracking & Storage
        E -.->|Metrics & Params| F[MLflow & DagsHub]
        E -->|Model Artifacts| G[(AWS S3)]
    end
    
    subgraph CI/CD & Deployment
        H[GitHub Actions] -->|Build & Push| I[Docker Image]
        I --> J[(AWS ECR)]
        J -->|Pull| K[AWS EC2<br/>Self-Hosted Runner]
        G -.->|Load Artifact| K
        K --> L[FastAPI Server]
        L --> M[Jinja2 HTML UI]
        L --> N[endpoints: /train, /predict]
    end
