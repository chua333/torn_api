import json
import time
import requests

from keys import torn_api_key
from datetime import datetime, timezone
from classes.faction import Faction
from classes.property import Property
from classes.company import Company


def main():
    # faction_id = input("Enter Faction ID: ")
    company_id = 100553
    # selections = input("Enter selections (or leave blank): ")
    selections = ""

    company = Company(company_id=company_id, selections=selections)
    company_details = company.get_company_details()
    print(company_details)


if __name__ == "__main__":
    main()
    