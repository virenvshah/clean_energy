import requests
# get world back data
import wbdata
from bs4 import BeautifulSoup

class WebScraper:
    def run(self):
        countries = wbdata.get_country()
        for country in countries:
            try:
                country_data = wbdata.get_data("EG.FEC.RNEW.ZS", country=country["id"])
            except Exception:
                print(f"Could not get data for country {country['name']}")

if __name__ == "__main__":
    web_scraper = WebScraper()
    web_scraper.run()
    