import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the website you want to download images from
website_url = 'https://worldtravelling.com/50-mind-bending-dark-comics-unravel-the-twisted-world-of-spaceboycantlol/28/?utm_source=Facebook&utm_medium=FB&utm_campaign=DUP%20GZM_WWide_Vidazoo_WB_SpaceBoy%20Comics_P4_NSO%20-%20vv8WT%20WT%20FB%20WW%20DS&utm_term=23858071072770342&layout=inf3&vtype=3&fbclid=IwAR2nmSGXQhaZMEfHWqlE0ExhZ9v9pzCKxSxBXqe42-fg8becpgjMLeeG1TE'

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
