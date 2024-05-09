from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# print(soup)

table = soup.find_all("table")[1]
print(table)
# # [1] is then used to select the second <table> element from the list.
#
# print(soup.find("table", class_ = "wikitable sortable"))
# # same as above
#
world_titles = table.find_all("th") # first table
world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)

#
df = pd.DataFrame(columns = world_table_titles)
# creates an empty Pandas DataFrame with columns specified by the world_table_titles variable
print(df)

column_data = table.find_all("tr") # each row in table
#
for row in column_data[1:]: # 第0行是一个[]，后面会报错
     row_data = row.find_all("td")
     individual_row_data = [data.text.strip() for data in row_data] # each element in the row
     # print(individual_row_data)
     # .text.strip() remove whitespace characters before and after text

     length = len(df) # how many rows on the dataframe now
     df.loc[length] = individual_row_data # adds the extracted data from the HTML table
     # (individual_row_data) into a new row of the DataFrame (df).
     # create a new row in the DataFrame and populate it with the extracted data.

print(df)

df.to_csv(r"/Users/amandadu/Desktop/coding/python/pandas/Companies.csv",index = False)
# remove index

# print(individual_row_data) # the last one
#
# length = len(df)





