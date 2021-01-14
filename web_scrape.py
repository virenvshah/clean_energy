import requests
import wbdata  # get world bank data
from app import db
from app.models import RenewableEnergyCountry
from bs4 import BeautifulSoup

class WebScraper:
    def run(self):
        db.create_all()
        # get list of all country codes
        countries = wbdata.get_country()
        for country in countries:
            country_data = []

            try:
                country_data = wbdata.get_data("EG.FEC.RNEW.ZS", country=country["id"])
            # Throws a NoneType error if country doesn't exist in world bank db
            except TypeError:
                print(f"Could not get data for country {country['name']}")

            for data_entry in country_data:
                if data_entry["value"]:
                    db_entry = RenewableEnergyCountry(
                        country=data_entry["country"]["value"], 
                        year=data_entry["date"],
                        renewable_energy_usage=data_entry["value"],
                    )
                    db.session.add(db_entry)
                db.session.commit()

if __name__ == "__main__":
    web_scraper = WebScraper()
    web_scraper.run()
    