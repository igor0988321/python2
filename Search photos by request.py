import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os

def search_and_download_images(query, num_images):
    search_url = f"https://www.google.com/search?hl=en&q={query}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(search_url, headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img", limit = num_images + 1)[1:]

    if not os.path.exists(query):
        os.makedirs(query)

    for i, img in enumerate(img_tags):
        try:
            img_url = img['src']
            img_response = requests.get(img_url)
            img_data = img_response.content

            img_path = os.path.join(query, f'{query}_{i + 1}.jpg')
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
            print(f"IMG {i + 1} downloaded to {img_path}")
        except Exception as e:
            print(f"Failed to download image: {i - 1}: {e}")


se=input("Enter your request: ")
count = int(input("How many images do you want to download? "))
search_and_download_images(se, count)