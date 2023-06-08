# Coreum Staking Monitor

A simple Python program for monitoring your personal Coreum staking rewards.

Note: The program screens the transaction history for *MsgWithdrawDelegatorReward* messages. If you spend your staking rewards, they will still be reflected in the exported CSV file.

More information about the Coreum Explorer API can be found on the [Coreum Docs Website](https://docs.coreum.dev/tutorials/explorer-api.html).

## Contents of exported CSV file
- Date
- Total Staking Reward (accumulated Delegator Reward withdrawals) [CORE]
- Average Daily Staking Reward (equals Total Staking Reward divided by the number of days since staking started) [CORE]
- Coreum Price [USD]
- Total Staking Reward Value [USD]
- Average Daily Staking Reward Value [USD]

## Usage
Simply insert / edit:
1. Your Coreum address
2. The date you first started staking
3. The path where the generated CSV file shall be stored.
4. Either run the program manually to take snapshots or run automated via eg. Cronjob.
