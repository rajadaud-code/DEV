import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to be scraped
url = "https://www.codewithharry.com"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully accessed the website.")
else:
    print(f"Failed to access the website. Status code: {response.status_code}")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Print the title of the webpage to verify parsing
print("Webpage Title:", soup.title.string)

# Find all the elements containing the data (e.g., video or blog titles)
titles = soup.find_all('h3')  # Assuming titles are in <h3> tags

# Extract the text from each title
title_list = [title.get_text(strip=True) for title in titles]

# Print the extracted titles
print("Extracted Titles:")
for title in title_list:
    print(title)

# Create a DataFrame from the extracted data
df = pd.DataFrame(title_list, columns=["Title"])

# Save the DataFrame to a CSV file
df.to_csv("codewithharry_titles.csv", index=False)

print("Data saved to codewithharry_titles.csv")
