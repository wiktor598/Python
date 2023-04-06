from urllib import response
import requests
from bs4 import BeautifulSoup 
from urllib.request import urlopen


url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url) #fetches data from url 
content = response.content # get all content from website
#print (status)

soup = BeautifulSoup(content, 'html.parser') #beautiful soupl will give a chance to parse
print(soup.title) #<title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) #UCI Machine Learning Repository: Data Sets
print(soup.body) #gives the whole page on the website
print(response.status_code) 

tables = soup.find_all('table',{'cellpadding' : '3'}) #targeting the table with cellpadding attribute with the value of 3
table = tables[0]
for td in table.find('tr').find_all('td'):
    #print(td.text)

        f = open("test2.txt", "a") #open given file 
        f.write(td.text) # write html code to file
        f.close() #close writer
