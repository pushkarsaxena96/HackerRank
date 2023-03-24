import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
#interlude = soup.find_all('section', {"class :", "content-section"})
interlude = soup.find_all(class_="content-section")
f = open("text.txt","w")
for item in interlude :
    print(item.get_text())
    f.write(item.get_text())

f.close()
    