import requests 
from bs4 import BeautifulSoup 

response = requests.get("https://www.unyp.cz/academic-programs/")
html_code = response.text 

soup = BeautifulSoup(html_code, "html.parser")

h3_tags = soup.find_all('h3')

for tag in h3_tags:
    print(tag.text)

programs = soup.find_all('h3', {"class": "wp-block-heading"})
for progr in programs:
    print(progr.text)