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
college_email = []
college_district = []
college_principal = []
college_office_no = []
college_personal_no = []
college_registrar = []

url = "http://dtemaharashtra.gov.in/"
for links in college_link:
    r = requests.get(url + links)
    webpage = bs(r.content, "lxml")
    # College Address
    addr = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id":"ctl00_ContentPlaceHolder1_lblAddressEnglish"})
    address = addr.get_text().rstrip('\r\n')
    college_address.append(address)
    # College Email
    mail = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id": "ctl00_ContentPlaceHolder1_lblEMailAddress"})
    email = mail.get_text().rstrip('\r\n')
    college_email.append(email)
    # College District
    dis = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id": "ctl00_ContentPlaceHolder1_lblDistrict"})
    district = dis.get_text().rstrip('\r\n')
    college_district.append(district)
    # College Principal
    princi = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id": "ctl00_ContentPlaceHolder1_lblPrincipalNameEnglish"})
    principal = princi.get_text().rstrip('\r\n')
    college_principal.append(principal)
    # College principal office number
    off_number = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id": "ctl00_ContentPlaceHolder1_lblOfficePhoneNo"})
    office_no = off_number.get_text().rstrip('\r\n')
    college_office_no.append(office_no)
    # College principal personal number
    per_number = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id": "ctl00_ContentPlaceHolder1_lblPersonalPhoneNo"})
    personal_no = per_number.get_text().rstrip('\r\n')
    college_personal_no.append(personal_no)
    # College Registrar
    reg_name = webpage.select("div.BodyDiv div.InnerBodyDiv table.AppFormTable")[0].find("span", attrs={
        "id": "ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish"})
    registrar = reg_name.get_text().rstrip('\r\n')
    college_registrar.append(registrar)


#print(college_address)
#print(college_email)
#print(college_district)
#print(college_principal)
#print(college_office_no)
#print(college_personal_no)
#print(college_registrar)


df_columns = ["Index", "Institute code", "College Name", "Address", "Email", "District", "Principal Name", "Office Number", "Personal Number", "Registrar Name"]
df = pd.DataFrame(list(zip(college_index,college_code,college_name,college_address,college_email,college_district,college_principal,college_office_no,college_personal_no,college_registrar)), columns=df_columns)
print(df.head())

df.to_csv('file.csv')
print("done")
