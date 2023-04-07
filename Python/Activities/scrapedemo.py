	
import requests
from bs4 import BeautifulSoup
	
res = requests.get("https://www.training-support.net/selenium/tables")	
content = res.content
	
soup = BeautifulSoup(content, "html.parser")
table = soup.find('table', {'id': 'sortableTable'})
	
for tr in table.find_all('tr'):    
    cells = tr.find_all('td')      
    row = [i.text for i in cells]
    print(row)     
