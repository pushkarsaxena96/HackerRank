import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
print(page.sstatus_code)
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('p')
print(data)