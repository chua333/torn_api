import json
import time
import requests

from keys import torn_api_key
from datetime import datetime, timezone
from faction import Faction


def main():
    # faction_id = input("Enter Faction ID: ")
    faction_id = 51042
    # selections = input("Enter selections (or leave blank): ")
    selections = ""

    faction = Faction(faction_id=faction_id, selections=selections)
    faction_ranks_dict = faction.get_faction_details()
    print(faction_ranks_dict)

    # # id: name
    # all_members_dict = get_faction_details()


if __name__ == "__main__":
    main()