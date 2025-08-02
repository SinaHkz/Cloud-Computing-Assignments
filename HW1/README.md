# Homework 1: Containerizing and Deploying an LLM Inference Service

**Course**: Cloud Computing - Spring 2025  
**Instructor**: [Dr. Farshad Khunjush](https://fkhunjush.github.io/website/)  
**Student**: Sina Hakimzadeh  
**Date**: March 19, 2025

## Problem Statement

The original question and instructions for this homework are available at:  
👉 [GitHub Homework Link](https://github.com/mmRoshani/cloud-computing-2025/tree/main/homeworks/one)

## Objective

This assignment focuses on containerizing a Flask-based sentiment analysis API using Docker and evaluating different deployment strategies. We explored:

- Running the app locally
- Containerizing with Docker
- Managing services with Docker Compose
- Scaling with Docker Swarm
- Automating deployment with GitHub Actions (Bonus)

## Summary of Tasks

### 1. Local Application Run
- A basic Flask API serving a pre-trained sentiment analysis model.
- Tested with HTTP requests and recorded latency using a shell script.

### 2. Docker Containerization
- Wrote a `Dockerfile` to define the container environment.
- Built the image and ran the container.
- Used `docker stats` and log files to gather performance metrics.

### 3. Docker Compose
- Defined services in `docker-compose.yml`.
- Mapped ports, set environment variables, and mounted volumes.
- Simplified multi-container management.

### 4. Docker Swarm
- Initialized a Swarm cluster and deployed the service.
- Scaled the service to 3 replicas.
- Analyzed improvements in latency and resource usage.

### 5. GitHub Actions (Bonus)
- Created a workflow to automatically build and push Docker images to Docker Hub on each commit to the `main` branch.

## Performance Metrics Summary

| Deployment        | CPU Usage | Memory   | Avg. Latency |
|------------------|-----------|----------|---------------|
| Local (No Docker) | 800%      | 5.7 GB   | 18.6 ms       |
| Docker Run        | 430%      | 270 MB   | 29.1 ms       |
| Docker Compose    | 415%      | 470 MB   | 29.02 ms      |
| Swarm (1 Replica) | 447.2%    | 358 MB   | 31.37 ms      |
| Swarm (3 Replicas)| 146%      | 406 MB   | 23.01 ms      |

## Conclusion

Docker technologies provide an efficient way to deploy and scale applications. While native runs are faster, Docker Swarm provides load balancing and high availability at the cost of increased complexity and overhead. GitHub Actions makes continuous deployment easier and more reliable.

