from fyers_api import fyersModel
from fyers_api import accessToken
import access_token as at

auth_code ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NzQwMzU0ODMsImV4cCI6MTY3NDA2NTQ4MywibmJmIjoxNjc0MDM0ODgzLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzM5MTI3Iiwib21zIjpudWxsLCJub25jZSI6InByaXZhdGUiLCJhcHBfaWQiOiIwOVBEWlpIMTIwIiwidXVpZCI6IjUzYWE3ODQ3MTUxNzRjZWFiN2FlOWE2OTc0MmVhOGI0IiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.1w_r3zrUCMUSdjOnv1sfrmNlSEEgA5OHdyH2hJIrJr8"

acc_tok=at.get_access_tkn(auth_code)

if acc_tok == "fail":
    at.gen_auth_code_url()
else:
    #print(acc_tok)
    with open('token.txt', 'w') as tk:
        tk.write(str(acc_tok))