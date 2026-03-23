from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter('request_count', 'Total API Requests')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency')