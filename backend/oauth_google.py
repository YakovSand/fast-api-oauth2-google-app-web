import urllib.parse

from config import settings

def generate_oauth_google_redirect_url():
    query_params = {
        "redirect_uri": "http://localhost:3000/auth/google",
        "client_id": settings.OAUTH_GOOGLE_CLIENT_ID,
        "response_type": "code",
        "scope": " ".join([
            "openid",
            "email", 
            "profile"
        ]),
        "access_type": "offline",
        # state": ...
    }

    # Encode the query parameters into a URL query string
    query_string = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)

    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{query_string}"