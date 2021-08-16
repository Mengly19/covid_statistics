# from dotenv import load_dotenv
# import os

import requests
from prettytable import PrettyTable
from datetime import datetime

# load_dotenv()

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    # 'x-rapidapi-key': os.getenv("API_KEY"),
    'x-rapidapi-key': "YOUR_API_KEY",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


today = datetime.now().strftime("%Y-%m-%d")



user_input = input("Enter the country : ").capitalize()


#get raw data from api 
raw_data = []

for i in response['response']:
    if i['day'] == today:
        date = datetime.strptime(i['time'], "%Y-%m-%dT%H:%M:%S+00:00")
        if user_input in i['country']:
            data = [
                    i['country'],
                    i['day'],
                    i['cases']['new'],
                    i['deaths']['new'],
                    i['cases']['active'],
                    i['cases']['recovered'],
                    i['cases']['total'],
                    ]
            raw_data.append(data)


# clean data
final_data = []

for i in raw_data:
    clean_data = []
    for j in i:
        if j is None:
            clean_data.append(0)
        else: 
            clean_data.append(j)
    final_data.append(clean_data)

# Create Table 
table = PrettyTable(['Country', 'Date', 'Total','Deaths','Active', 'Recovered','Total of cases'])
table.add_rows(final_data)
print(table)