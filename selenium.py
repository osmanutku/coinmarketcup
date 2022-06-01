from selenium import webdriver
import time

URL = "https://coinmarketcap.com/"

browser = webdriver.Firefox()
browser.get(URL)
time.sleep(3)

name, price =[],[]
x1="//*[@id='__next']/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr["
x2="]/td[3]/div/a/div/div/p"
y1="//*[@id='__next']/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr["
y2="]/td[4]/div/a/span"

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False# bu javascript kodu sayfayı en aşağı indirmek için
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

try:
    for i in range(1,13):
        xpath=x1+str(i)+x2
        coin_name=browser.find_element_by_xpath(xpath)
        name.append(coin_name.text)
        value=browser.find_element_by_xpath(y1+str(i)+y2)
        price.append(value.text)
        #time.sleep(4)
        print(coin_name.text + " : " + value.text)
except Exception as e:
    print("hata : "+str(e))


browser.close()
