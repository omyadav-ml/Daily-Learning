# Github Profile Scraping
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/omyadav-ml"


req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")

meta_tag = scraper.find("meta", property="og:image")

if meta_tag:
    profile_picture = meta_tag["content"]
    print("Profile Picture URL:", profile_picture)
else:
    print("Profile picture not found!")
