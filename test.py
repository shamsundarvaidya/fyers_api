
from fyers_api import fyersModel
from fyers_api import accessToken
import access_token as at


client_id = "09PDZZH120-100"


acc_tok = ""

with open('token.txt') as tk:
    acc_tok = tk.read()

#print(acc_tok)

fyers = fyersModel.FyersModel(client_id=client_id, token=acc_tok,log_path="./")

data = {"symbols":"NSE:NIFTY50-INDEX"}
nif_data = fyers.quotes(data)['d'][0]['v']
nif_ltp = nif_data['lp']
print(fyers.quotes(data)['d'][0]['v']['lp'])