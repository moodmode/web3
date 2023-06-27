from web3 import Web3
import pandas as pd

df = pd.read_excel('MM.xlsx')
wallet_addresses = df['Address'].tolist()
print(len(wallet_addresses))
i = 0
for address in wallet_addresses:
    i += 1
    print(f'Начинаю работу с кошельком {address} осталось {int(i/len(wallet_addresses)*100)} %')
