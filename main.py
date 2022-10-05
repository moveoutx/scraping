import bs4
import requests


CONTS = ['UX/UI', 'UX', 'UI', 'designer']
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

URL = "https://habr.com"

response = requests.get(URL, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")
for article in articles:
    conts = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    conts = [cont.text.strip().split() for cont in conts]
    for cont in conts:
        for co in cont:
            if co in CONTS:
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                title = article.find("h2").find("span").text
                result = f"{title} ==> {URL}{href}"
                print(result)
