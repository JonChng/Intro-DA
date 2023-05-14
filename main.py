import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
soup = BeautifulSoup(web.text, "html.parser")

column_names = []
data_dict = {}

names = soup.find_all("th")
for i in names:
    column_names.append(i.text)

for i in column_names:
    data_dict[i] = []

rank = soup.find_all("td", class_='data-table__cell csr-col--rank')
for i in rank:
    r = i.text.split(":")[1]

    data_dict[i.text.split(":")[0]].append(r)


rank = soup.find_all("td", class_='data-table__cell csr-col--school-name')
for i in rank:
    r = i.text.split(":")[1]

    data_dict[i.text.split(":")[0]].append(r)

rank = soup.find_all("td", class_='data-table__cell csr-col--school-type data-table__cell--hidden-mobile')
for i in rank:
    r = i.text.split(":")[1]

    data_dict[i.text.split(":")[0]].append(r)

rank = soup.find_all("td", class_='data-table__cell csr-col--right')
for i in rank:
    r = i.text.split(":")[1]

    data_dict[i.text.split(":")[0]].append(r)

print(data_dict)



