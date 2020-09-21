import pandas as pd
import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.flipkart.com/search?q=laptopd&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup=BeautifulSoup(page.content , 'html.parser')
items=soup.find(class_='_1HmYoV hCUpcT')
list=items.find_all(class_='_1UoZlX')

datalist=[]
for box in list:
    dict={}
    dict['name']=box.find("div",{"class":"_3wU53n"}).text.strip()
    #price=[i.find("span",class_="_89yzn").get_text() for i in a ]
    dict['rating']=box.find("div","class":"hGSR34").get_text()
    dict['price']=box.find("div",{"class":"_1vC4OE _2rQ-NK"}).text.strip()
    datalist.append(dict)
print(dict)

df=pd.DataFrame(datalist)
print(df)

df.to_csv('flipkart.csv')
