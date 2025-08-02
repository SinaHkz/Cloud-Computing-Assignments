# Homework 3: Exploring Modern Cloud Paradigms – Kubernetes, OpenFaaS, and Ray

**Course**: Cloud Computing – Spring 2025  
**Instructor**: [Dr. Farshad Khunjush](https://fkhunjush.github.io/website/)  
**Student**: Sina Hakimzadeh  
**Due Date**: June 15, 2025

**Homework Link**: [GitHub Homework 3 Instructions](https://github.com/mmRoshani/cloud-computing-2025/tree/main/homeworks/third)

---

## Prerequisites & Installation

Tools used:
- `kubectl`
- `kind`
- `faas-cli`
- `helm`
- `Lens` (Kubernetes GUI)

Installed via Homebrew and verified with version commands.

---

## Part 1: Kubernetes with kind

### Cluster Creation
- Created a local single-node Kubernetes cluster using `kind`.
- Verified using `kubectl cluster-info` and `kubectl get nodes`.

### Nginx Deployment & Exposure
- Deployed `nginx` via `Deployment` and `Service` YAML files.
- Exposed using NodePort (30080) and accessed using port forwarding to port 8080.

### Scaling
- Scaled `nginx` deployment to 3 replicas with `kubectl scale`.

### Monitoring with Prometheus & Grafana
- Installed `kube-prometheus-stack` via Helm.
- Used port-forwarding to access:
  - **Grafana**: `http://localhost:3000`
  - **Prometheus**: `http://localhost:9090`

### Kubernetes Visualization
- Used **Lens IDE** to explore resources visually.
- Observed core components and deployed workloads.

---

## Part 2: Serverless Deployment with OpenFaaS

### Setup
- Installed OpenFaaS using Helm with `openfaas` and `openfaas-fn` namespaces.
- Enabled basic auth and port-forwarded the gateway.

### Function Creation
- Created `to-uppercase` function using `python3-http` template.
- Code: Converts input string to uppercase.

### Build & Deployment
- Built the image with `faas-cli`.
- Pushed to Docker Hub due to Community Edition limitations.
- Deployed via `faas-cli deploy`.

### Function Invocation
- Invoked using CLI:
  ```bash
  echo -n "hello world" | faas-cli invoke to-uppercase --gateway http://127.0.0.1:8080
  ```
## Function Monitoring (Lens)

- Wrote a Python load script to stress-test the function.
- Monitored CPU usage (~0.38 cores) and memory (~100MB) via Lens dashboards.
- Confirmed pod stability and resource efficiency during repeated invocations.

---

## Part 3: Distributed Computing with Ray on Kubernetes

### Ray Cluster Setup

- Installed Ray using KubeRay Helm charts on kind (ARM64-compatible).
- Successfully deployed both head and worker pods.

### Running Ray Apps

- Copied Python scripts into the Ray head pod using `kubectl cp`.
- Executed both a simple test (`ray.init()`) and a MapReduce-style word count using `ray.remote`.

### Ray Dashboard

- Accessed via:
  ```bash
  kubectl port-forward ray-head-pod 8265:8265
  ```

- Tracked job execution, node metrics, task distribution, and logs via the Ray Dashboard.

---

### Lens Monitoring

- Verified that Ray **head** and **worker** pods were in the **Running** state.
- Observed **active CPU usage**, confirming real-time distributed computation within the Ray cluster.

---

### Ray vs. OpenFaaS Comparison

| Feature             | Ray                                      | OpenFaaS                               |
|---------------------|-------------------------------------------|-----------------------------------------|
| Architecture        | Head and worker nodes (stateful)          | Stateless HTTP-triggered functions      |
| Execution Model     | Tasks and actors (supports statefulness)  | Stateless Functions-as-a-Service (FaaS) |
| Use Cases           | ML training, data pipelines, inference     | APIs, microservices, event-driven tasks |
| Resource Handling   | Distributed scheduling and memory         | Autoscaling, container-based execution  |
| Best For            | Long-running, parallel, stateful workloads| Lightweight, short-lived tasks          |


## Final Cluster Architecture
```
Local macOS Host
 └── Docker
     └── kind Cluster ("cloud-homework")
         ├── Core Kubernetes Components
         ├── Nginx Deployment (port 30080)
         ├── Monitoring Stack (Prometheus + Grafana)
         ├── OpenFaaS Platform
         │   ├── Gateway
         │   └── Functions (to-uppercase)
         └── Ray Cluster
             ├── Head Node + Dashboard (port 8265)
             └── Worker Node(s)
```
## Conclusion

This homework provided hands-on experience with:

- **Kubernetes** for container orchestration.
- **OpenFaaS** for serverless, stateless function deployment.
- **Ray** for distributed, stateful task execution.

It offered valuable insights into how these modern cloud-native technologies work both **individually** and **together** in real-world cloud systems.
