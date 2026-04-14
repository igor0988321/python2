import pyshorteners

url = input("Enter the link: ").strip()
s = pyshorteners.Shortener()

try:
    short_url = s.isgd.short(url)
    print(f"Short URL: {short_url}")
except Exception as e:
    print(f"Error: {e}")