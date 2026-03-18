import requests
import random

url = "http://quotes.toscrape.com/api/quotes?page=1"

result = requests.get(url)
content = result.json()

random_quote = random.choice(content['quotes'])

print(f'Author: {random_quote['author']['name']}')
print(f"Text: {random_quote['text']}\n")
