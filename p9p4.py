from bs4 import BeautifulSoup
import requests

index = int(input("Vvedit nomer u spisku: "))

response = requests.get("https://coinmarketcap.com")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-631098c-0 ilZTOW"})
    soup_list1 = soup.find_all("p", {"class": "sc-c1554bc0-0 eWrlhi coin-item-name"})

    res1 = soup_list1[index].get_text()
    res = soup_list[index].find("span")
    print(f"Valuta: {res1}, vartist: {res.text}")