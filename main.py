import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib



url = "https://www.iplt20.com/auction/2022"

r =requests.get(url)

# print(r)
htmlContent = r.content
# print(htmlContent) # show all html element

soup = BeautifulSoup(r.text,"lxml")
# print(soup) # print whole html content as written as

table  = soup.find("table",class_="ih-td-tab auction-tbl")
# print(table)

# title = soup.find_all("th") # show only head of the table
# print(title) # print th data

tabletitle = table.find_all("th") # all table header
# print(tabletitle) # print all with tag name in list from

tableHead =[]
for i in tabletitle:
    name = i.text # all i element of table store in variable name
    tableHead.append(name) # append into above empty list

# print(tableHead) #only text will print

df = pd.DataFrame(columns= tableHead) # alldata print on a df dataset 
# print(df) # coloumn name add into data set and it shows data frame empty

#get data
tableRows = table.find_all("tr")
# print(tableRows) # pribt all table data with tag after tabel head

for  i in tableRows[1:]:
    first_td = i.find_all("td")[0].find("div", class_ ="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]# in index 0it is a img
    # print(data) # all table data in from of list
    row = [tr.text for tr in data]
    # print(row) # print all rows data in form \n in list format

    row.insert(0, first_td)
    # add into dataframe
    l = len(df)
    df.loc[l] = row
    
# print(df) # print all gtable data

df.to_csv("ipl aution start 2022.csv") # create csv in same folder
 
