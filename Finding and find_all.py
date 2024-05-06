from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

soup_find = soup.find("div")
# print(soup_find)
# soup.find("div"): This finds the first <div> element in the HTML document and returns it as a bs4.element.Tag object.
# The result you got is the first <div> element in the HTML document along with all its child elements. When you use soup.find("div"),
# BeautifulSoup returns the first <div> element in the HTML document along with all its child elements.

# soup_find_all = soup.find_all("div")
# # soup.find_all("div"): This finds all <div> elements in the HTML document and returns them as a list of bs4.element.Tag objects.
# print(soup_find_all)

# soup_find_all = soup.find_all("div",class_ = "col-md-12")
#  get a list of all <div> elements with the class "col-md-12". two times
# print(soup_find_all)

# soup_find_p = soup.find_all("p",class_ ="lead")
# print(soup_find_p)

# soup.find_all("p",class_ ="lead").text # wrong, cause find_all doesn't have a text attribute, we need to change to find
soup_find_text = soup.find("p",class_ ="lead").text.strip()
print(soup_find_text)

soup_find_th = soup.find_all("th")
print(soup_find_th)
#
# soup_find_td = soup.find_all("td")
# print(soup_find_td)

soup_find_teamname = soup.find("th").text.strip()
# soup.find("th") returns only the first <th> element found in the HTML document.
print(soup_find_teamname)