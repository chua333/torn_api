import json
import requests

from keys import torn_api_key


def get_property_details():
    try:
        with open("endpoints_v1.json", "r") as f:
            endpoints = json.load(f)

        # property_id = input("Enter Property ID: ")
        property_id = 12345
        # selections = input("Enter selections (or leave blank): ")
        selections = ""

        api_endpoint = endpoints["property"]
        url = api_endpoint.format(property_id=property_id, selections=selections, api_key=torn_api_key)

        response = requests.get(url)
        property_data = response.json()
        property_data = property_data.get("property", {})

        owner_id = property_data.get("owner_id")
        property_type = property_data.get("property_type")
        property_index = {
            0: "Shack",
            1: "Trailer",
            2: "Apartment",
            3: "Semi-Detached House",
            4: "Beach House",
            5: "Chalet",
            6: "Villa",
            7: "Penthouse",
            8: "Villa",
            9: "Mansion",
            10: "Ranch",
            11: "Palace",
            12: "Castle",
            13: "Private Island",
            14: "Eagle Island",
            15: "Silo X17",
            16: "Drakkar Sea Fort",
            17: "Queen Eleanor",
            18: "Cerium Temple",
            19: "Trekant Tower",
            20: "Iron Fist Hill",
            21: "USS Bloodbath",
            22: "Royal Penthouse",
            23: "Presidential Bunker",
            24: "Maidengrave",
            25: "St. Pauls Abbey"
        }
        property_type_name = property_index.get(property_type, "Unknown")
        happy = property_data.get("happy", 0)
        upkeep = property_data.get("upkeep", 0)
        upgrades = property_data.get("upgrades", [])
        staff = property_data.get("staff", [])
        rented = property_data.get("rented", False)
        users_living = property_data.get("users_living", "Unknown")
        users_living = users_living.split(",")

    except Exception as e:
        print("Request failed:", e)
        return