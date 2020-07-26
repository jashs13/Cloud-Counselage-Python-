import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# Load the webpage
r = requests.get("http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=3&RegionName=Mumbai")

# Convert to a BS object
webpage = bs(r.content, "lxml")
#print(webpage.prettify())

table = webpage.select("div.InnerBodyDiv table.DataGrid")[0]
table_content = table.find_all("tr")
table_content = table_content[2:]
#print(table_content[0].prettify())
#print(table_content[0].find_all("a")[1]['href'])    # getting institude link

college_index,college_link,college_code,college_name = [],[],[],[]
for td in table_content:
    index = td.find("td", attrs={"class":"Item"}).get_text()
    college_index.append(index)
    link = td.find("td", attrs={"class":"Item"}).next_sibling()[1]['href']
    college_link.append(link)
    code = td.find("td", attrs={"class":"Item"}).next_sibling()[1].get_text()
    college_code.append(code)
    name = td.find("td", attrs={"class":"Item"}).find_next('td').find_next('td').text.strip()
    college_name.append(name)

#print(college_index)
#print(college_link)
#print(college_code)
#print(college_name)




college_address = []

url = "http://dtemaharashtra.gov.in/"
for links in college_link:
    r = requests.get(url + links)
    webpage = bs(r.content, "lxml")
    addr = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={"id":"ctl00_ContentPlaceHolder1_lblAddressEnglish"})
    address = addr.get_text().rstrip('\r\n')
    college_address.append(address)


print(college_address)


'''
df_columns = ["Index", "Institute code", "College Name", "Address"]
df = pd.DataFrame(list(zip(college_index,college_code,college_name,college_address)), columns=df_columns)
print(df.head())

df.to_csv('file1.csv')
print("done")
'''