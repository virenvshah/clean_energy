from app import db

class RenewableEnergyCountry(db.Model):
    country = db.Column(db.String(128), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    renewable_energy_usage = db.Column(db.Float)

    def __repr__(self):
        prefix = f"<{self.country}, {self.year}"
        suffix = f"renewable energy usage -> {self.renewable_energy_usage}>"
        return prefix + ", " + suffix


