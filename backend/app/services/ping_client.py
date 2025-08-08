import httpx, time

class PingClient:
    def __init__(self, base_url: str, env_id: str, client_id: str, client_secret: str):
        self.base_url = base_url.rstrip("/")
        self.env_id = env_id
        self.client_id = client_id
        self.client_secret = client_secret
        self._token = None
        self._exp = 0

    async def _token(self) -> str:
        if self._token and self._exp - time.time() > 60:
            return self._token
        token_url = f"{self.base_url}/v1/oauth/token"
        data = {"grant_type": "client_credentials"}
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.post(token_url, data=data, auth=(self.client_id, self.client_secret))
            r.raise_for_status()
            js = r.json()
            self._token = js["access_token"]
            self._exp = time.time() + int(js.get("expires_in", 3600))
            return self._token

    async def _get(self, path: str, params: dict | None = None):
        token = await self._token()
        url = f"{self.base_url}/v1/environments/{self.env_id}{path}"
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.get(url, params=params, headers={"Authorization": f"Bearer {token}"})
            r.raise_for_status()
            return r.json()

    async def list_users(self, limit: int = 200):
        return await self._get("/users", params={"limit": limit})

    async def list_groups(self, limit: int = 200):
        return await self._get("/groups", params={"limit": limit})
