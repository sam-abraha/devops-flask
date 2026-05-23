# DevOps CI/CD Flask Application

A production-style DevOps project demonstrating a complete CI/CD workflow using Flask, Docker, GitHub Actions, Nginx, VPS deployment, Prometheus and Grafana.

The application automatically runs tests, builds Docker images, pushes them to Docker Hub, and deploys updates to a live VPS environment through an automated CI/CD pipeline.

---

# Live Demo

Production Deployment:

🌍 https://velvetclouds.de

---

# Overview

This project focuses on real-world DevOps workflows rather than complex business logic.

It demonstrates how modern applications are:

- containerized with Docker
- automatically tested
- continuously integrated
- continuously deployed
- reverse proxied through Nginx
- secured with HTTPS
- hosted on a VPS

---

# Features

- REST API built with Flask
- Health Check Endpoint
- Automated Testing with Pytest
- Docker Containerization
- GitHub Actions CI/CD Pipeline
- Docker Hub Image Registry
- Automated VPS Deployment via SSH
- Nginx Reverse Proxy
- HTTPS with Let's Encrypt SSL
- Live Production Deployment
- Prometheus Metrics Collection
- Grafana Monitoring Dashboard
- Container-to-Container Networking

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns application message |
| GET | `/metrics` | Exposes Prometheus metrics |

---

# Architecture

```text
Git Push
   ↓
GitHub Actions
   ↓
Pytest
   ↓
Docker Build
   ↓
Docker Hub Push
   ↓
SSH Deploy to VPS
   ↓
Docker Container Restart
   ↓
Nginx Reverse Proxy
   ↓
HTTPS Domain
```
---

# Monitoring & Observability

The project includes a monitoring stack using Prometheus and Grafana.

Prometheus scrapes application metrics from the Flask `/metrics` endpoint, while Grafana visualizes system and application performance metrics such as:

- total HTTP requests
- request rate
- request latency
- CPU usage
- memory consumption

# Monitoring Architecture

```text
Flask App
   ↓ exposes /metrics
Prometheus
   ↓ scrapes metrics
Grafana
   ↓ visualizes dashboards
```