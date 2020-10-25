import requests
from bs4 import BeautifulSoup

list_books = []
for i in range(1,76):

    website_url = "https://www.amazon.com.au/s?rh=n%3A4851626051&page={}&qid=1603500586&ref=lp_4851626051_pg_2"
    website_request = requests.get(website_url.format(i))
    
    soup = BeautifulSoup(website_request.text, "lxml")
    books = soup.select(".sg-col-inner")
    print(len(books))
    print(books)
    #list_books.append(books)


