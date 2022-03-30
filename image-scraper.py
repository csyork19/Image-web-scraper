import requests
import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://www.sports-reference.com/cbb/players/paolo-banchero-1.html'

# Make a get request to get the pages content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
images = soup.find_all("img")

number = 0
for image in images:
    image_src = image['src']
    if "sports-reference" in image_src:
        # This will take the image src/url and save the file with the 2nd parameter as the name
        urllib.request.urlretrieve(image_src, str("player" + str(number)))
        number += 1
