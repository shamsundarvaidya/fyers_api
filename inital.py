from fyers_api import fyersModel
from fyers_api import accessToken
import access_token as at

auth_code ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NzUxNTcwNDgsImV4cCI6MTY3NTE4NzA0OCwibmJmIjoxNjc1MTU2NDQ4LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUzM5MTI3Iiwib21zIjpudWxsLCJub25jZSI6InByaXZhdGUiLCJhcHBfaWQiOiIwOVBEWlpIMTIwIiwidXVpZCI6ImY2ZWI0Y2JmYmNmYjQxZjg4ZjkwMDg2MzZkYzhkMWRjIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.D_eOzvt4QsBZ4UuAsYe_TbCq5wm_wGxbaJXMc6Cpcp4"

acc_tok=at.get_access_tkn(auth_code)

if acc_tok == "fail":
    at.gen_auth_code_url()
else:
    #print(acc_tok)
    with open('token.txt', 'w') as tk:
        tk.write(str(acc_tok))