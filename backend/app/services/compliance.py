from datetime import datetime, timedelta

def mfa_enabled(user: dict) -> bool:
    # Placeholder heuristic. Adjust based on your PingOne user shape.
    enrolled = (user.get("mfa") or {}).get("enrolled") or []
    return len(enrolled) > 0

def parse_last_seen(user: dict) -> datetime | None:
    # Adjust to your env (activities API or profile attribute)
    # Return None if unknown
    return None

def compute_findings(users_payload: dict, activities_payload: dict | None = None) -> list[dict]:
    findings = []
    users = users_payload.get("_embedded", {}).get("users", [])
    for u in users:
        email = u.get("email") or u.get("username")
        if not mfa_enabled(u):
            findings.append({
                "type": "MFA_MISSING", "severity": "HIGH",
                "subject": email, "evidence": {"userId": u.get("id")}
            })
        last_seen = parse_last_seen(u)
        if not last_seen or last_seen < (datetime.utcnow() - timedelta(days=90)):
            findings.append({
                "type": "STALE_ACCOUNT", "severity": "MEDIUM",
                "subject": email, "evidence": {"last_seen": str(last_seen)}
            })
    return findings
