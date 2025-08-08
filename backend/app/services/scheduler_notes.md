# Scheduler Notes

For AWS EventBridge + Lambda:
- Create a rule (e.g., `rate(1 hour)`) to invoke `worker` Lambda.
- Worker Lambda queries tenants due for sync and calls the PingOne APIs.
- Use Secrets Manager (per-tenant) to fetch Ping client credentials at runtime.
