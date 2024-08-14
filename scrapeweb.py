import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Get the HTML content
url = "https://codewithharry.com"
r = requests.get(url)
htmlContent = r.content

# Step 2: Parse the HTML content
soup = BeautifulSoup(htmlContent, 'html.parser')

# Step 3: HTML Tree traversal and data extraction

# Get the title of the HTML page
title = soup.title.string if soup.title else "No title found"

# Get all paragraphs on the page
paras = [para.get_text() for para in soup.find_all('p')]

# Get the first paragraph
first_para = soup.find('p').get_text() if soup.find('p') else "No paragraph found"

# Get the classes of the first paragraph
first_para_classes = soup.find('p')['class'] if soup.find('p') else "No classes found"

# Find all elements with the class "lead"
lead_paras = [para.get_text() for para in soup.find_all("p", class_="lead")]

# Get all the anchor tags of the page and their corresponding links
anchors = soup.find_all('a')

# Collect all unique links
all_links = set()
for link in anchors:
    href = link.get('href')
    if href and href != '#':
        full_link = "https://www.codewithharry.com" + href
        all_links.add(full_link)

# Convert the set of links to a list for saving
all_links = list(all_links)

# Step 4: Save the data to an Excel file using pandas

# Create a dictionary to organize the data
data = {
    "Title": [title],
    "First Paragraph": [first_para],
    "First Paragraph Classes": [first_para_classes],
    "Lead Paragraphs": [lead_paras],
    "Links": all_links
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)

print("Data saved to scraped_data.xlsx")

# Convert the set of links to a list for saving
all_links = list(all_links)

# Step 4: Save the data to an Excel file using pandas

# Create a dictionary to organize the data
data = {
    "Title": [title],
    "First Paragraph": [first_para],
    "First Paragraph Classes": [first_para_classes],
    "Lead Paragraphs": [lead_paras],
    "Links": all_links
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)

print("Data saved to scraped_data.xlsx")

# Step 4: Save the data to an Excel file using pandas

# Create a dictionary to organize the data
data = {
    "Title": [title],
    "First Paragraph": [first_para],
    "First Paragraph Classes": [first_para_classes],
    "Lead Paragraphs": [lead_paras],
    "Links": all_links
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)

print("Data saved to scraped_data.xlsx")
