import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website you want to download images from
website_url = 'https://<YOURE WEBSITE ADDRESS>'

# Directory to save downloaded images
output_dir = 'downloaded_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# GET request to the website
response = requests.get(website_url)
response.raise_for_status()

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags and extract their URLs
img_tags = soup.find_all('img')
img_urls = [urljoin(website_url, img['src']) for img in img_tags if 'src' in img.attrs]

# Download the images
for img_url in img_urls:
    img_filename = os.path.basename(img_url)
    img_path = os.path.join(output_dir, img_filename)
    
    print(f"Downloading: {img_url} -> {img_path}")
    
    try:
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        print(f"Downloaded: {img_path}")
    except Exception as e:
        print(f"Failed to download: {img_url} - {str(e)}")
