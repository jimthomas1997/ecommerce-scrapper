import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv


page=requests.get('https://www.indiabookstore.net/categories/art')
#print(page.status_code)
soup=BeautifulSoup(page.content,'html.parser')
item=soup.find_all("div",class_="col-md-3 col-xs-6 text-center")
#print(item)
# list=item.find_all("div",class_="col-md-3 col-xs-6 text-center ")
# print(list)
book=[i.find("div",class_="truncateName").text.strip() for i in item]
author=[i.find("div",class_="truncateAuthor").text.replace(" ","").replace("\n","").replace("by","").strip() for i in item]
rating=[i.find("div",class_="userStoreSpecificRatingBox").text.replace("\n"," ").strip() for i in item]
print(book)
print(author)
print(rating)

book=pd.DataFrame({
    "Book":book,
    "Author":author,
    "Rating":rating
})
print(book)
book.to_csv('book.csv')
writer = pd.ExcelWriter('book.xlsx', engine='xlsxwriter')
book.to_excel(writer, sheet_name='Sheet1',index=True)
writer.save()
reader = pd.read_excel('C:\\Users\\JIM\\PycharmProjects\\BookScrape\\book.xlsx')
readernew=[['index','Rating']]
plt.plot(readernew)
print(reader.head())

# x = []
# y = []
#
# with open('book.txt','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
#
# plt.plot(x,y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()


