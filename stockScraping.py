import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Download the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
response = requests.get(url)
html_data = response.text

# Step 2: Parse the HTML data
soup = BeautifulSoup(html_data, 'html.parser')

# Question 1: Extract the content of the title attribute
title_attribute = soup.find('title').text
print(f"Title Attribute: {title_attribute}")

# Step 3: Extract the table and store it into a DataFrame
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

# Find the table
table = soup.find("table")

# Extract table rows
for row in table.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text.strip()
    Open = col[1].text.strip()
    high = col[2].text.strip()
    low = col[3].text.strip()
    close = col[4].text.strip()
    adj_close = col[5].text.strip()
    volume = col[6].text.strip()
    
    amazon_data = pd.concat([amazon_data, pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

# Print the first five rows of the DataFrame
print("\nFirst Five Rows of amazon_data DataFrame:")
print(amazon_data.head())

# Question 2: Names of the columns in the DataFrame
print("\nColumn Names:")
print(amazon_data.columns.tolist())

# Question 3: Open of the last row
last_row_open = amazon_data.iloc[-1]['Open']
print(f"\nOpen of the Last Row: {last_row_open}")
