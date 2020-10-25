from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import sqlite3 as sql

conn = sql.connect("pre_orders.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS books(ID INTEGER PRIMARY KEY, title TEXT,price TEXT,desc_quote TEXT)")
conn.commit()



#booktobefest (pre-orders)

#fiction-list = "https://www.booktopia.com.au/books-online/fiction/cF-p1.html?sorter=sortorder-en-dsc"

url = 'https://www.booktopia.com.au/booktoberfest-2020-life-style/promo2999.html'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()


soup = bs(webpage, "lxml")
books = soup.select(".col")


for book in books:
    #book title
    book_title = book.select("h2")
    for title in book_title:
        cur.execute("INSERT INTO books (title) VALUEs (?)",(title.text,))
        conn.commit()
    #book_price
    book_price = book.select(".sale-price")
    for price in book_price:
        cur.execute("INSERT INTO books (price) VALUEs (?)", (str(price.text),))
        conn.commit()
        print(price.text)
    #book description
    book_description = book.select(".review-quote")
    for desc in book_description:
        cur.execute("INSERT INTO books (desc_quote) VALUEs (?)", (str(f'"{desc.text}"'),))
        conn.commit()
        print(desc.text)
    break



cur.execute("SELECT * FROM books")
data = cur.fetchall()

for d in data:
    print(d)