from fyers_api import fyersModel
from fyers_api import accessToken
import access_token as at

auth_code ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NzUzMTc0MTYsImV4cCI6MTY3NTM0NzQxNiwibmJmIjoxNjc1MzE2ODE2LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzM5MTI3Iiwib21zIjpudWxsLCJub25jZSI6InByaXZhdGUiLCJhcHBfaWQiOiIwOVBEWlpIMTIwIiwidXVpZCI6ImM1OWE1ZGNiNDQzODQ0NGJhZGY1NGM0MWM1YzUxNjkxIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.v7E6MWxkVau0rrN6fHsMyuP00AcwdlM2CoQVT-UnwjY"

acc_tok=at.get_access_tkn(auth_code)

if acc_tok == "fail":
    at.gen_auth_code_url()
else:
    #print(acc_tok)
    with open('token.txt', 'w') as tk:
        tk.write(str(acc_tok))