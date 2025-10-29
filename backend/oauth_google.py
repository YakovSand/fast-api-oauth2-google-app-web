import urllib.parse

from config import settings

# Function to generate Google OAuth 2.0 redirect URL
def generate_oauth_google_redirect_url():
    # Define the query parameters for the OAuth 2.0 authorization request
    # See https://developers.google.com/identity/protocols/oauth2/web-server#creatingclient
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