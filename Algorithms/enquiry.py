import csv
import requests
from bs4 import BeautifulSoup

#train_no = int(input("Enter the train number: "))
#dat = int(input("Enter the Traveling Date YYYYMMDD : "))
url = "https://runningstatus.in/status/11112-on-20180301"
r=requests.get(url)
data=r.text

soup=BeautifulSoup(data,"html.parser")
## Extracting the column-names
tables = soup.find("table", {"class" : "table table-striped table-bordered"})
records = []
for row in tables.find('thead') :
    column = tables.find('tr').text.strip().split("\n")
    
records.append(column)

data = tables.find('tbody')
#Extracting the rows
for rows in tables.find('tbody'):
    for row in data.find_all('tr') :
        records.append(list(row.text.strip().split("\n")))
        
print(records)

        
   