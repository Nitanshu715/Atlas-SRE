\# Failure Scenarios – ATLAS SRE Platform



\## Scenario 1: Pod Failure and Self-Healing



\### What Happened

A production application pod (`atlas-api`) was manually deleted to simulate a runtime failure.



\### Detection

The failure was immediately detected through:

\- Kubernetes pod status change

\- A brief dip in CPU usage visible in Grafana dashboards



\### Mitigation

Kubernetes automatically recreated the pod using the Deployment controller, restoring the desired replica count without manual intervention.



\### Observability Evidence

\- Grafana dashboards showed a temporary resource usage fluctuation

\- Pod returned to `Running` state within seconds



\### Outcome

The application remained available, demonstrating Kubernetes self-healing and the effectiveness of the observability stack.



