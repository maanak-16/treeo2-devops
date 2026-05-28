# TreeO2 DevOps Pipeline

This project demonstrates a Jenkins DevOps pipeline for a sample TreeO2 Backend API.

## Project Description

TreeO2 is represented as a backend API that supports tree monitoring, farmer records, health checks, and basic monitoring data. The aim of this project is to demonstrate a complete DevOps pipeline using Jenkins.

## Technologies Used

- Python
- FastAPI
- Docker
- Jenkins
- pytest
- Bandit
- GitHub

## Jenkins Pipeline Stages

1. Build
2. Test
3. Code Quality
4. Security
5. Deployment
6. Release
7. Monitoring

## Run Locally

```bash
python -m uvicorn app.main:app --reload