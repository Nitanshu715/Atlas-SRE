<p align="center">
  <img src="https://raw.githubusercontent.com/Nitanshu715/Atlas-SRE/main/Atlas-SRE-Logo.PNG" alt="ATLAS-SRE Banner" />
</p>

<h1 align="center">ATLAS-SRE</h1>

<p align="center">
  <b>Production-Grade DevOps & Site Reliability Engineering Platform</b><br/>
  <i>Designed, deployed, observed, and broken on purpose.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-EKS-orange?style=for-the-badge&logo=amazonaws"/>
  <img src="https://img.shields.io/badge/Kubernetes-Production-blue?style=for-the-badge&logo=kubernetes"/>
  <img src="https://img.shields.io/badge/SRE-Observability%20Focused-purple?style=for-the-badge&logo=grafana"/>
</p>

---

## 🌍 Project Overview

**ATLAS-SRE** is a full end-to-end **Site Reliability Engineering (SRE) focused DevOps project**
built on **AWS Elastic Kubernetes Service (EKS)**.

This project is intentionally **not** a tutorial clone, not a YAML dump, and not a feature-heavy
microservices demo.

Instead, ATLAS-SRE was built to answer a single production question:

> *Can this system survive failures while remaining observable and stable?*

Everything in this repository exists to support that goal.

---

## 🎯 Core Objectives

ATLAS-SRE was designed around the following objectives:

- Build a real Kubernetes cluster on AWS (not local)
- Deploy a production application with proper isolation
- Implement ingress and cloud-native networking
- Add full observability (metrics + dashboards)
- Simulate real production failures
- Verify self-healing and recovery
- Document reliability outcomes clearly

---

## 🧠 SRE Mindset Behind the Project

Traditional DevOps projects often stop after deployment.

ATLAS-SRE goes further by focusing on:

- **Reliability over features**
- **Observability before scale**
- **Failure as a first-class citizen**
- **Automation instead of manual recovery**

This mirrors how modern SRE teams operate in real organizations.

---

## 🏗️ Architecture Deep Dive

```text
User
 └── AWS Application Load Balancer (ALB)
      └── Kubernetes Ingress Controller
           └── Production Namespace
                └── atlas-api Deployment
                     ├── Pod 1
                     └── Pod 2
                          ↓
                Prometheus Metrics Collection
                          ↓
                    Grafana Dashboards
```

### Key Architectural Decisions

- **AWS EKS** was chosen for managed control-plane reliability
- **Namespaces** isolate production and observability workloads
- **ALB Ingress** provides cloud-native traffic routing
- **Minimal microservices** avoid unnecessary complexity

---

## ⚙️ Technology Stack

### Cloud & Infrastructure
- AWS EKS
- AWS EC2 Managed Node Groups
- AWS Application Load Balancer
- IAM Roles & Policies

### Container & Orchestration
- Docker
- Kubernetes

### Observability
- Prometheus (metrics scraping)
- Grafana (visualization)

### Tooling
- kubectl
- eksctl
- Helm
- Git & GitHub

---

## 🚀 Application Deployment

The application (`atlas-api`) is a lightweight service designed to:

- Generate traffic
- Consume resources predictably
- Expose metrics naturally
- Fail safely

Deployment characteristics:
- Replica-based scaling
- Resource requests & limits
- Readiness and liveness probes
- Zero manual restarts required

---

## 🌐 Networking & Ingress

- External traffic enters through AWS ALB
- Kubernetes Ingress routes traffic to services
- Services forward traffic to pods
- Load balancing handled automatically

This setup reflects **real cloud-native networking**, not port-forward hacks.

---

## 📊 Observability Implementation

Observability was treated as a **first-class requirement**, not an afterthought.

### Metrics Collected
- CPU utilization
- Memory utilization
- Pod health
- Namespace-level resource usage

### Dashboards Used
- Kubernetes Cluster Overview
- Compute Resources (Cluster)
- Compute Resources (Pods)
- Networking metrics

Grafana was deployed **inside the cluster** and accessed securely,
which aligns with real production security practices.

---

## 🧪 Failure Scenarios & Reliability Testing

### Scenario: Pod Failure

A production pod was manually deleted to simulate runtime failure.

#### Detection
- Kubernetes immediately detected pod termination
- Grafana showed a brief CPU usage dip

#### Mitigation
- Deployment controller recreated the pod automatically
- Desired replica count restored without intervention

#### Outcome
- Application remained available
- No manual recovery required
- Self-healing behavior verified

Full documentation available in:
`docs/failure-scenarios.md`

---

## 🛠️ Challenges Faced & Solutions

### Grafana Access in AWS
- AWS Managed Grafana unavailable in region
- Solution: Self-hosted Grafana inside EKS

### LoadBalancer Port Conflicts
- Multiple ports caused LB routing issues
- Solution: Clean service recreation with explicit ports

### Security Group Restrictions
- External traffic blocked by default SGs
- Solution: Verified via port-forwarding (production-safe)

These challenges reflect **real-world cloud debugging**, not lab environments.

---

## 📁 Repository Structure

```text
Atlas-SRE/
├── services/
│   └── api-service/
├── k8s/
│   └── api/
├── observability/
├── docs/
│   └── failure-scenarios.md
└── README.md
```

---

## ✅ What This Project Demonstrates

- Real AWS EKS operations
- Kubernetes reliability patterns
- Observability-driven debugging
- Failure injection & recovery
- Production engineering mindset

This single project replaces multiple shallow DevOps demos.

---

## 🏁 Final Thoughts

ATLAS-SRE is intentionally focused.

No unnecessary tools.  
No artificial scale claims.  
No buzzword overload.

Just:
- Real infrastructure
- Real failures
- Real recovery
- Real observability

This is how modern systems are actually built and maintained.

