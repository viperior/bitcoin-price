import urllib, json

url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
response = urllib.urlopen(url)
data = json.loads(response.read())

print("Current Bitcoin price:")
bitcoin_usd_price = "$" + str(round(float(data["bpi"]["USD"]["rate"].replace(",", "")), 2)) + " USD"
bitcoin_price_timestamp = "Last updated: " + str(data["time"]["updated"])

print(bitcoin_usd_price)
print(bitcoin_price_timestamp)
