from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')

soup.find('table')

table = soup.find_all('table')[1]
#print(table)
soup.find('table', class_ = 'wikitable sortable')

world_titles = table.find_all('th')

world_titles =[title.text.strip() for title in world_titles]

df = pd.DataFrame(columns = world_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    raw_data = row.find_all('td')
    individual_row_data =[data.text.strip() for data in raw_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


print(df)
df.to_csv("example.csv",index=False)


          

