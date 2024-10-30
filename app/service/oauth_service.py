import httpx
from app.config.settings import Settings

settings = Settings()

class OAuthService:

    async def get_token(self):
        async with httpx.AsyncClient() as client:
            url = settings.oauth2_token_uri

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            data = {
                'grant_type': 'client_credentials',
                'client_id': settings.oauth2_client_id,
                'client_secret': settings.oauth2_client_secret
            }

            response = await client.post(url, headers=headers, data=data)

            if response.status_code == 200:
                oauth = response.json()
                access_token = oauth.get('access_token')
                print(f"Access Token: {access_token}")
                return f"Bearer {access_token}"
            else:
                print(f"Error: {response.status_code} - {response.text}")