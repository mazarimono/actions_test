import requests 
import pandas as pd 

bitflyer = "https://api.bitflyer.com/v1/"

r = requests.get(bitflyer + "getticker")

time_stamp = r.json()["timestamp"]
bid = r.json()["best_bid_size"]
ask = r.json()["best_ask_size"]
bid_depth = r.json()["total_bid_depth"]
ask_depth = r.json()["total_ask_depth"]

now_data = [time_stamp, bid, ask, bid_depth, ask_depth]

cols_name = ["time_stamp", "bid", "ask", "bid_depth", "ask_depth"]

new_df = pd.DataFrame(now_data).T 
new_df.iloc[0, 0] = pd.to_datetime(new_df.iloc[0, 0])
new_df.columns = cols_name 

df = pd.read_csv("./data/bit.csv", index_col=0)

dff = pd.concat([df, new_df]).reset_index(drop=True)

dff.to_csv("./data/bit.csv")

print("finish")
