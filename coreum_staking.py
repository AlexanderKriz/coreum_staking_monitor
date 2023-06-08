import requests
import json
from datetime import date
import csv
import os

query = """{
        messages_by_address(args: {addresses: "{INSERT COREUM WALLET ADDRESS HERE}", offset: "0", types: "{}"}) {
        value
        type
        transaction_hash}
        }"""

url = 'https://hasura.mainnet-1.coreum.dev/v1/graphql'
r = requests.post(url, json={'query': query})
json_data = json.loads(r.text)

withdraw_arr = []
delegate_arr = []
stake_rewards = []
index = 0
for item in json_data["data"]["messages_by_address"]:
    if item.get('type') == "cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward":
        withdraw_arr.append(item.get('transaction_hash'))
    elif item.get('type') == "cosmos.staking.v1beta1.MsgDelegate":
        delegate_arr.append([int(json_data["data"]["messages_by_address"][index]["value"]["amount"]["amount"])/1000000, item.get('transaction_hash')])
    index += 1
    
for item in range(len(delegate_arr)):
    for items in range(len(withdraw_arr)):
        if delegate_arr[item][1] == withdraw_arr[items]:
            stake_rewards.append(delegate_arr[item][0])

start = date(2023, 3, 29) # ENTER STAKING STARTING DATE HERE
end = date.today()
stakedays = (end - start).days
stake_rew_sum = int(sum(stake_rewards))

price_url = 'https://api.coinpaprika.com/v1/tickers/core-coreum'
price = requests.get(price_url)
json_price = json.loads(price.text)
current_price = json_price["quotes"]["USD"]["price"]
current_value = current_price * sum(stake_rewards)
daily_value = current_value / stakedays

header = ["Date", "Total Staking Reward", "Avg. Daily Staking Reward", "Coreum Price (USD)", "Staking Reward Value (USD)", "Avg. Daily Staking Reward Value (USD)"]
data = [date.today().strftime("%d/%m/%Y"), stake_rew_sum, int(stake_rew_sum / stakedays), "%.3f" % current_price, int(current_value), int(daily_value)]

path = 'C:/Path/to/CSV file/coreum_staking_stats.csv'

if os.path.exists(path) == True:
    with open(path, 'a') as file:
        export = csv.writer(file)
        export.writerow(data)
else: 
    with open(path, 'w') as file:
        export = csv.writer(file)
        export.writerow(header)
        export.writerow(data)