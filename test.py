
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
response = fyers.quotes(data)
#print(response)
if response['s'] == "error":
    print(response['message'])
else:
    nif_data = response['d'][0]['v']
    nif_ltp = nif_data['lp']
    nif_chg = nif_data['ch']
#print(fyers.quotes(data)['d'][0]['v']['ch'])
    print(f'LTP : {nif_ltp}||ch:{nif_chg}')