import csv
import httpx

API_URL_COINMARKETCAP = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=1500&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap'
API_URL_SIMPLESWAP = 'https://simpleswap.io/api/v3/currencies?fixed=false&includeDisabled=false'

with httpx.Client() as client:
    response1 = client.get(API_URL_COINMARKETCAP)
    response2 = client.get(API_URL_SIMPLESWAP)
    
    data_coinmarketcap = response1.json()
    data_simpleswap = response2.json()
    data_coinmarketcap = data_coinmarketcap['data']['cryptoCurrencyList']

    data_coin = {}
    data_simpl = {}
    list_not_coins = []
    for coin in data_coinmarketcap:
        for k, v in coin.items():
            if k in ['name', 'symbol', 'slug', 'quotes']:
                if v is None:
                    v = 'none'
                    
                if k == 'quotes':
                    btc_volume = v[0]['volume24h']
                    eth_volume = v[1]['volume24h']
                    usd_volume = v[2]['volume24h']
                    data_coin.setdefault(k, []).append((btc_volume, eth_volume, usd_volume))
                    continue
                    
                data_coin.setdefault(k, []).append(v.lower())

    for simpl in data_simpleswap:
        for k, v in simpl.items():
            if k in ['name', 'symbol']:
                if v is None:
                    v = 'none'
                
                data_simpl.setdefault(k, []).append(v.lower())
    
    for v_name, v_symbol, v_slug, v_quotes in zip(data_coin['name'], data_coin['symbol'], data_coin['slug'], data_coin['quotes']):
        for v_name1, v_symbol1 in zip(data_simpl['name'], data_simpl['symbol']):
            if v_name in [v_name1, v_symbol1] or v_symbol in [v_name1, v_symbol1] or v_slug in [v_name1, v_symbol1]:
                break
        else:
            list_not_coins.append((v_name, v_quotes))
    
    with open('not_coin.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Монета', 'BTC', 'ETH', 'USD'])

        for row in sorted(list_not_coins, key=lambda x: x[1][0], reverse=True):
            token_name = row[0]
            values = row[1]
            writer.writerow([token_name, *values])

    print("Данные успешно записаны.")