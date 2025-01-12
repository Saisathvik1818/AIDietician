import requests
from bs4 import BeautifulSoup
import os

# Function to fetch images from Bing search
def fetch_bing_images(query, num_images):
    q=query+" food"
    url = f"https://www.bing.com/images/search?q={q}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', class_='mimg')
    #print(img_tags)

    # Download images
    for i, img_tag in enumerate(img_tags[:num_images]):
        try:
            img_url = img_tag['src']
            img_data = requests.get(img_url).content
            with open(f"{query}.jpg", 'wb') as f:
                f.write(img_data)

        except:
            pass

# Define the food items you want to search for
f=open('foodlist.txt','r')
f=f.read()
f=f.split('\n')
print(f)
food_items = f

# Number of images to fetch for each food item
num_images_per_item = 1

# Fetch images for each food item
for item in food_items:
    fetch_bing_images(item, num_images_per_item)
