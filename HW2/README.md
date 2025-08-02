# Homework 2: Distributed Data Processing for Federated Learning using Hadoop and Spark

**Course**: Cloud Computing – Spring 2025  
**Instructor**: [Dr. Farshad Khunjush](https://fkhunjush.github.io/website/)  
**Student**: Sina Hakimzadeh  
**Date**: April 2025

## Problem Statement

The full instructions and problem description can be found here:  
👉 [Homework 2 Instructions on GitHub](https://github.com/mmRoshani/cloud-computing-2025/tree/main/homeworks/two)

---

## Part 1: Foundational Knowledge & Environment Setup

### Technologies Overview

- **MapReduce**: A programming model for distributed computing, using `Map`, `Shuffle`, and `Reduce` phases to process data.
- **Hadoop**:
  - **HDFS**: Hadoop’s file system, storing data in blocks distributed across machines.
  - **YARN**: Resource manager and scheduler in Hadoop clusters.
- **Spark**:
  - Uses **RDDs** and **DataFrames** for distributed, in-memory data processing.
  - Offers much faster processing than MapReduce, especially for iterative and ML tasks.

### Environment

- Simulated Hadoop and Spark clusters via Docker and Docker Compose.
- Ran MapReduce jobs and Spark programs on the provided datasets.

---

## Part 2: Comparative Analysis

### Speed and Efficiency

- **Hadoop**: Writes intermediate results to disk → higher disk I/O and slower performance.
- **Spark**: Performs in-memory computations → significantly faster, especially for iterative tasks like ML.

### Data Handling

| Feature        | Hadoop MapReduce | Apache Spark         |
|----------------|------------------|----------------------|
| Storage        | HDFS             | HDFS / In-Memory     |
| Data Structure | Key-Value pairs  | RDDs / DataFrames    |
| Speed          | Disk I/O based   | In-memory optimized  |
| Use Cases      | Batch jobs       | ML, Streaming, ETL   |

### Use Cases

- **Hadoop**: Best for large-scale batch processing with fault tolerance.
- **Spark**: Ideal for real-time analytics, ML, and interactive queries.

---

## Part 3: Practical Application in Federated Learning

### Federated Learning Concept

- Clients train models locally and send encrypted updates to a central server.
- Central server aggregates updates without accessing raw data → privacy preserved.

### Hadoop: Initial Aggregation

- Used simulated Hadoop cluster via Docker.
- Ran a MapReduce job using Python mapper and reducer scripts.
- Discovered a bug with handling CSV headers in distributed contexts → fixed in updated mapper logic.
- Output written to HDFS, accessed via command-line.

### Spark: Global Model Update

- Installed `spark-submit` manually inside the container.
- Processed MapReduce output with PySpark to simulate federated model aggregation.
- Three rounds of federated averaging performed using Spark RDDs.
- Used Spark Web UI for monitoring.

### Execution Output Example

```text
Initial Global Average: 41.5468

--- Round 1 ---
client1 updated average: 38.4661
client2 updated average: 42.0802
client3 updated average: 44.9797
Global Average after Round 1: 42.1111

--- Round 2 ---
client1 updated average: 38.5865
client2 updated average: 42.6685
client3 updated average: 44.3791
Global Average after Round 2: 41.4664

--- Round 3 ---
client1 updated average: 37.2381
client2 updated average: 41.3851
client3 updated average: 44.9858
Global Average after Round 3: 41.5806
```
## Analysis and Evaluation

### Performance Comparison

- **Hadoop Job Timing**:
  - **Real time**: ~30.6s
  - **User time**: ~6.6s
  - **System time**: ~0.9s

- **Map-Only Mode**:
  - Reduced time to ~23.5s
  - Indicates significant overhead from the reducer phase and container startup.

- **Spark Execution**:
  - **Total time**: ~10.6s
  - Demonstrates Spark’s efficiency in iterative tasks due to in-memory computation.

### Resource Utilization

- **Hadoop**:
  - Higher overhead due to disk-based computation, job scheduling, and container simulation via Docker.

- **Spark**:
  - Lower latency and higher memory usage.
  - Significantly faster thanks to in-memory RDDs and reduced I/O.

---

## Conclusion

This assignment demonstrated how **Hadoop** and **Spark** support distributed data processing and federated learning:

- **Hadoop** excels in batch processing, data pre-processing, and fault-tolerant initial aggregation.
- **Spark** shines in iterative machine learning applications like federated learning due to its fast, in-memory computations and easy scalability.

Both technologies are valuable in cloud-based ML pipelines:
- **Spark** is recommended for real-time, request-based learning.
- **Hadoop** is more suitable for pre-processing large raw datasets.

