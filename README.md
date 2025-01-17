# Задание 2

## Структура проекта
**main.py** - Основной скрипт, который находит монеты, отсутствующих у Simpleswap. И с суточными оборотами этих монет, взятых с Coinmarketcap.
**not_coin.csv** - Файл с данными

## Описание проекта
Напиши скрипт, который используя данные эндпоинта
https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=1500&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap
выведет монеты, которых нет здесь:
https://simpleswap.io/api/v3/currencies?fixed=false&includeDisabled=false.
Результатом выполнения задания является список монет, отсутствующих у Simpleswap, приведенный в виде таблицы с суточными оборотами этих монет, взятых с Coinmarketcap и отсортированный по суточному обороту с Coinmarketcap от большего к меньшему.

## Проверка проекта
1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/XHackerFinnX/NoCoin.git
   cd NoCoin
   ```
2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Запустите файл:**
   ```bash
   python main.py
   ```
