from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-631098c-0 ilZTOW"})
    #for elem in soup_list:
    #    print(elem)
    res = soup_list[0].find("span")
    print(res.text)