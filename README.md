<p align="center">
  <img src="https://user-images.githubusercontent.com/placeholder/atlas-banner.png" alt="ATLAS-SRE Banner" />
</p>

<h1 align="center">ATLAS-SRE</h1>

<p align="center">
  <b>Production-Grade DevOps & Site Reliability Engineering Platform on AWS</b>
</p>

<p align="center">
  <i>Built to prove reliability, not just deployment.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-EKS-orange?style=for-the-badge&logo=amazonaws"/>
  <img src="https://img.shields.io/badge/Kubernetes-Production-blue?style=for-the-badge&logo=kubernetes"/>
  <img src="https://img.shields.io/badge/Observability-Prometheus%20%7C%20Grafana-purple?style=for-the-badge&logo=grafana"/>
</p>

---

## 🧠 What is ATLAS-SRE?

ATLAS-SRE is a production-focused DevOps & Site Reliability Engineering project built on AWS EKS.

This project prioritizes:
- Reliability over feature count
- Observability from day one
- Failure handling and recovery
- Real-world Kubernetes operations

---

## 🏗️ Architecture Overview

User Traffic  
→ AWS Application Load Balancer (ALB)  
→ Kubernetes Ingress  
→ Production Namespace  
→ atlas-api Pods  
→ Metrics collected via Prometheus  
→ Visualized in Grafana

---

## ⚙️ Technology Stack

- AWS (EKS, ALB, IAM)
- Docker
- Kubernetes
- Prometheus
- Grafana
- Git & GitHub

---

## 🔍 Observability

Grafana dashboards provide:
- Cluster-level metrics
- Namespace-level resource usage
- Pod CPU and memory monitoring

Accessed securely using port-forwarding.

---

## 🧪 Failure Testing

A production pod was manually deleted to simulate failure.

Kubernetes automatically:
- Detected the failure
- Recreated the pod
- Restored the desired state

This behavior was observed live via Grafana dashboards.

---

## 📄 Documentation

- `docs/failure-scenarios.md` – detailed SRE failure analysis

---

## 🎯 What This Project Proves

- Real AWS EKS deployment experience
- Kubernetes reliability and self-healing
- Production-grade observability
- SRE mindset and debugging skills

---

## 🧠 Final Note

ATLAS-SRE is intentionally focused.

No unnecessary tools.  
No artificial scaling claims.  
Just real infrastructure, real failures, and real recovery.

