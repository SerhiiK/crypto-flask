import requests, json

def req_current_price(crypto_name, currency):
    """
    function get current price of cryptocurrency in selected currency
    """
    payload = {'ids': crypto_name ,'vs_currencies': currency }
    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {'accept': 'application/sjon'}

    r = requests.get(url, params=payload, headers=headers)
    data = r.json()
    return data[crypto_name][currency]
    

if __name__ == "__main__":
    price = req_current_price('bitcoin', 'usd')
    print(price)
