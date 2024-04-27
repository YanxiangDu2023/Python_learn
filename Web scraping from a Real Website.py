# BeautifulSoup and Requests
from bs4 import BeautifulSoup
# 这两行代码导入了BeautifulSoup和requests库，用于网页数据的抓取和解析。

import requests

url = 'https://www.scrapethissite.com/pages/forms/'

#这一行定义了要抓取的网页的URL地址。

page = requests.get(url)

# requests.get(url)发送一个GET请求来获取指定URL的网页内容，并将结果保存在result变量中。
print(page)

#`<Response [200]>`表示网页请求成功。HTTP状态码200表示请求已成功。这意味着服务器已成功处理了请求。

result = BeautifulSoup(page.text, 'html')

#在requests库中，response对象有一个.text属性，它返回服务器响应的文本内容。
#在这个例子中，我们使用requests.get(url)获取了网页的响应对象，然后通过.text属性获取了网页的文本内容。

#对于BeautifulSoup的解析器参数，你可以使用不同的解析器来解析HTML文本。常用的解析器有：
#"html.parser"：这是BeautifulSoup内置的HTML解析器，通常情况下都可以使用
#"html.parser"作为解析器参数，因为它是BeautifulSoup内置的解析器，不需要安装额外的库。

print(result.prettify())
# The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string,
# with a separate line for each tag and each string:









