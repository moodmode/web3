from web3 import Web3
import pandas as pd

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/03d821a7a38f49f59611f8e5bb6b23c1'))

main_wallet_address = '0xe83f5444067DB9A0E7EcE74B59bff06754d41713'

main_wallet_private_key = '7df72a06f4e96afd2bad4d563200efca7f9b8fc538e79d67769b58aea89522af'

df = pd.read_excel('MM.xlsx')

wallet_addresses = df['Address'].tolist()

bnb_amount = input('Укажите желаемое количество BNB')  # Укажите желаемое количество BNB
bnb_to_wei_ratio = 10**18  # 1 BNB = 10^18 wei

# Преобразование количества BNB в wei
value_wei = int(bnb_amount * bnb_to_wei_ratio)
def send_bnb(wallet_address):
    # Проверка наличия достаточного количества BNB на главном кошельке
    balance = w3.eth.get_balance(main_wallet_address)
    print(balance)
    if float(balance) < float(bnb_amount):
        print(f"Ошибка: Недостаточно BNB на главном кошельке для отправки на адрес: {wallet_address}")
        return

    # Создание транзакции отправки BNB
    tx = {
        'to': wallet_address,
        'value': value_wei,
        'gas': 21000,
        'gasPrice': w3.toWei('5', 'gwei'),  # Укажите желаемую цену газа
        'nonce': w3.eth.getTransactionCount(main_wallet_address),
        # Добавьте другие необходимые параметры транзакции
    }

    # Подпись транзакции
    signed_tx = w3.eth.account.signTransaction(tx, private_key=main_wallet_private_key)

    # Отправка подписанной транзакции на блокчейн
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Ожидание подтверждения транзакции
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Обработка результата транзакции
    if receipt['status']:
        print(f"BNB успешно отправлен на адрес: {wallet_address}")
        # Добавьте дополнительную логику после успешной отправки BNB
    else:
        print(f"Ошибка при отправке BNB на адрес: {wallet_address}")

# Отправка BNB на каждый кошелек
for address in wallet_addresses:
    send_bnb(address)
