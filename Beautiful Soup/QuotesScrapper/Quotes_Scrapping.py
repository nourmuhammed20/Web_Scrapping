import requests
from bs4 import BeautifulSoup
import csv
import os

topics = ["love","inspirational","life","humor","books","reading","friendship","friends","truth"]
for topic in topics:
    url = requests.get(f"http://quotes.toscrape.com/tag/{topic}")
    quotes_deatils=[]
    def main(url):
        src = url.content
        soup = BeautifulSoup(src, "lxml")

        quotes = soup.find_all("div", {"class": "quote"})
        def get_quote_details(quote):
            quote_content = quote.find('span', {'class': 'text'}).text
            author = quote.find('small', {'class': 'author'}).text
            tags = [tag.text for tag in quote.find_all('a', {'class': 'tag'})]
            quotes_deatils.append({"Quote":quote_content,"Author":author,"Tags":tags})
        for quote in quotes:
            get_quote_details(quote)


    directory = f"csv_files/{topic}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f'csv_files/{topic}/{topic}.csv', 'w', newline='') as output_file:
        keys = ['Quote', 'Author', 'Tags']
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(quotes_deatils)
        print("File created successfully.")

main(url)