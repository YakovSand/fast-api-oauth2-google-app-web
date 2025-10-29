from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from oauth_google import generate_oauth_google_redirect_url
from config import settings
from typing import Annotated
from fastapi import Body
import aiohttp
import jwt

router = APIRouter(prefix="/auth")

@router.get("/google/url")
def get_google_oauth_redirect_url():
    uri = generate_oauth_google_redirect_url()
    return RedirectResponse(uri, status_code=302)

@router.post("/google/callback")
async def google_oauth_callback(code: Annotated[str, Body(embed=True)]):
    google_token_url = "https://oauth2.googleapis.com/token"
    print("qqq_qqq")
    print(f"{code=}")
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    async with aiohttp.ClientSession() as session:
        async with session.post(google_token_url, data={
            "code": code,
            "client_id": settings.OAUTH_GOOGLE_CLIENT_ID,
            "client_secret": settings.OAUTH_GOOGLE_CLIENT_SECRET,
            "redirect_uri": "http://localhost:3000/auth/google",
            "grant_type": "authorization_code",
        }, headers=headers) as resp:
            try:
                token_response = await resp.json() 
            except Exception:
                text_body = await resp.text()
                return {"error": "Failed to parse response from Google", "body": text_body, "status": resp.status}

            if resp.status != 200:
                return {"error": "Failed to obtain access token from Google", "details": token_response}
        
        print("ppp_ppp")                        
        token_response = await resp.json()
        print("ttt_ttt")
        print(f"{token_response=}")
        id_token = token_response.get("id_token")
        user_data = jwt.decode(id_token, algorithms=["RS256"], options={"verify_signature": False})

    return {"user_data": user_data}
    # return {"message": "Callback received", "code": code}