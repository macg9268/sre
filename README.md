# SRE Reliable API Project

## Overview
This project simulates a production-ready service with monitoring, logging, and automation.

## Observability
- Metrics: Prometheus
- Dashboards: Grafana


## Features
- FastAPI service with failure simulation
- Prometheus metrics


## Incident Scenarios
1. High latency (/slow)
2. Error spike (/error)

### High latency
- Endpoint: /slow
- Result: latency spike in Prometheus
