import requests
from bs4 import BeautifulSoup
import urllib.request

# Prompt the user for the URL to scrape
url = input("Enter the URL to scrape: ")

# Send a request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product items on the page
products = soup.find_all('div', {'class': 'sd-item'})

# Loop through each product item and extract the name, price, and image URL
for product in products:
    try:
        name = product.find('h3', {'class': 'sd-item-title'}).text
    except:
        name = ''
    try:
        price = product.find('div', {'class': 'sd-item-price'}).text
    except:
        price = ''
    try:
        img = product.find('div', {'class': 'sd-item-img'}).find('img')['src']
        urllib.request.urlretrieve(img, f"{name}.jpg")
    except:
        img = ''


   
    # Print the results for each product item
    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"Image URL: {img}\n")
