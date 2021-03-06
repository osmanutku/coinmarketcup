import requests
from bs4 import BeautifulSoup
#import time

URL = "https://coinmarketcap.com/currencies/"
coin=["bitcoin","ethereum","tether","usd-coin","bnb","cardano","xrp","binance-usd","solana","dogecoin","polkadot",
      "wrapped-bitcoin","tron","avalanche","multi-collateral-dai","shiba-inu","polygon","unus-sed-leo","litecoin","cronos",
      "near-protocol","uniswap","ftx-token","bitcoin-cash","stellar","monero","chainlink","ethereum-classic","cosmos",
      "algorand","flow","vechain","hedera","apecoin-ape","decentraland","internet-computer","tezos","elrond-egld","kucoin-token","the-sandbox"]

def veri_alPrice (url):
    try:
#        time.sleep(1)
        page=requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        if page.status_code == 200:
            div_price = soup.find_all("div", attrs={"class": "priceValue"})
            value1=div_price[0].find("span").text
            div_rank = soup.find_all("div", attrs={"class": "namePill namePillPrimary"})
            value2=div_rank[0].text
            return value1,value2
        else:
            return page.status_code
    except Exception as e:
        return e

for i in range(len(coin)):
    urlplas=URL+coin[i]
    text, text2=veri_alPrice(urlplas)
    print(text2+".  " + coin[i]+" :   "+text)
