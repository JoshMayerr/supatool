# def initialize_spotify():
#     client_id = "enter your client_id here"
#     client_secret = "enter your client_secret here"

#     auth_headers = {
#         "client_id": client_id,
#         "response_type": "code",
#         "redirect_uri": "http://localhost:7777/callback",
#         "scope": "user-library-read"
#     }

#     webbrowser.open("https://accounts.spotify.com/authorize?" +
#                     urlencode(auth_headers))


# def get_spotify_token(code: str):
#     encoded_credentials = base64.b64encode(
#         client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

#     token_headers = {
#         "Authorization": "Basic " + encoded_credentials,
#         "Content-Type": "application/x-www-form-urlencoded"
#     }

#     token_data = {
#         "grant_type": "authorization_code",
#         "code": code,
#         "redirect_uri": "http://localhost:7777/callback"
#     }

#     r = requests.post("https://accounts.spotify.com/api/token",
#                       data=token_data, headers=token_headers)

#     token = r.json()["access_token"]
#     return token
# def construct_spotify_auth_headers(raw_spec: dict):
#     scopes = list(raw_spec["components"]["securitySchemes"]["oauth_2_0"]
#                   ["flows"]["authorizationCode"]["scopes"].keys())
#     access_token = util.prompt_for_user_token(scope=",".join(scopes))
#     return {"Authorization": f"Bearer {access_token}"}
