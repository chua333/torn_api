import json
import time
import requests

from keys import torn_api_key
from datetime import datetime, timezone
from faction import Faction
from property import Property


def main():
    # faction_id = input("Enter Faction ID: ")
    property_id = 3438671
    # selections = input("Enter selections (or leave blank): ")
    selections = ""

    property = Property(property_id=property_id, selections=selections)
    property_details = property.get_property_details()
    print(property_details)


if __name__ == "__main__":
    main()