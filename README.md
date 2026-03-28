# sre
# SRE Reliable API Project

## Overview
This project simulates a production-ready service with monitoring, logging, and automation.

## Observability
- Metrics: Prometheus
- Dashboards: Grafana
- Alerts: Prometheus rules

## Features
- FastAPI service with failure simulation
- Prometheus metrics
- Dockerized deployment
- Terraform infrastructure
- Jenkins CI/CD pipeline

## Incident Scenarios
1. High latency (/slow)
2. Error spike (/error)

### High latency
- Endpoint: /slow
- Result: latency spike in Prometheus
- Alert triggered