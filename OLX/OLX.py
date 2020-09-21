import pandas as pd
import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.olx.in/items/q-mobile?isSearchCall=true')
#print(page.status_code)   --> if its 200 then u r good to scrap otherwise NO!!

# second way to check if the site can be scrapped is go to the robots.txt and if it is disallow:  then u can scrape
#if it is disallow:/   then u cant
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
title=soup.title.get_text()
#print(title)
anchor=soup.find_all('a')
#print(anchor)
a=soup.find_all("div",class_="IKo3_")
# for i in a:
#     print(i.get_text())  ---> these 2 lines are used to print when we use find_all

for i in a:
    print(i.find("span",class_="_89yzn").get_text())

price=[i.find("span",class_="_89yzn").text.replace("₹","Rs.").strip() for i in a ]
details=[i.find("span",class_="_2tW1I").text.strip() for i in a ]
location=[i.find("span",class_="tjgMj").text.strip() for i in a ]
print(price)
print(details)
print(location)

olx=pd.DataFrame({
    'Price':price,
    'Details':details,
    'Location':location
})

print(olx)

olx.to_csv('olx.csv')

