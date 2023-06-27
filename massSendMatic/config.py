
#то что ниже обязательно заполнить своими данными
privat_key="8f8"

#то что ниже желательно настроить под себя

#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 1 #минимальная 
timeoutMax = 3 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 1 #минимальная 
timeoutTehMax = 3 #максимальная



#то что ниже можно менять только если понимаешь что делаешь
request_kwargs = {"timeout": 120}



rpc_links = {
    'polygon': 'https://polygon-rpc.com/',
    'arbitrum': 'https://arb1.arbitrum.io/rpc',
    'optimism':  'https://rpc.ankr.com/optimism',
    'bsc': 'https://bscrpc.com',
    'fantom': 'https://rpc.ftm.tools/',
    'avax': 'https://api.avax.network/ext/bc/C/rpc',
}
