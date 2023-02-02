from fyers_api import accessToken
import webbrowser

client_id = "09PDZZH120-100"
secret_key = "IJMWK4ZAEJ"
redirect_uri = "https://localhost"
grant_type = "authorization_code"
state = "private"
nonce = "private"
scope = ""

auth_code = "none"


session=accessToken.SessionModel(client_id=client_id,
    secret_key=secret_key,redirect_uri=redirect_uri, 
    response_type="code", grant_type=grant_type,
    state=state,scope=scope,nonce=nonce)

def gen_auth_code_url():
    res = session.generate_authcode()
    print(res)
    print("Complete the login in browser to get auth code")
    webbrowser.open(res, new=2)
    return



def get_access_tkn(auth_code):
    session.set_token(auth_code)
    response = session.generate_token()

    if response["s"] == "ok":
        print("saving token to file")
        return response["access_token"]
        
    else:
        print(response["message"])
        return "fail"

