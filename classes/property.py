import json
import requests

from keys import torn_api_key


class Property:
    def __init__(self, property_id: int, selections: str = ""):
        """
        The init function will initialise using:
        1. Property ID
        2. Selections (optional)

        Property ID must be supplied by the user.
        Selections are optional as the default non-selections returns most of the details.
        Selections can be specified as a comma-separated list of fields to include.

        Args:
            property_id (int): The Torn City property ID to query.
            selections (str, optional): Extra selections to include (default is "").
        """
        try:
            self.property_id = property_id
            self.selections = selections

            with open("endpoints_v1.json", "r") as f:
                self.endpoints = json.load(f)

            api_endpoint = self.endpoints["property"]
            url = api_endpoint.format(property_id=property_id, selections=selections, api_key=torn_api_key)

            response = requests.get(url)
            self.property_data = response.json()

        except Exception as e:
            print("Request failed:", e)

    def get_property_details(self):
        """

        Returns:
            dict: A dictionaries mapping property attributes to their values:
                - "owner_id" (int): Property ID
                - "property_type" (int): Property Type (refer to index below)
                - "happy" (int): Property Happiness
                - "upkeep" (int): Property Upkeep
                - "upgrades" (list): Property Upgrades
                - "staff" (list): Property Staff
                - "rented" (bool): Is Property Rented
                - "users_living" (list): Users Living in Property

        """
        try:
            property_data = self.property_data.get("property", {})

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

            return {
                "owner_id": owner_id,
                "property_type": property_type_name,
                "happy": happy,
                "upkeep": upkeep,
                "upgrades": upgrades,
                "staff": staff,
                "rented": rented,
                "users_living": users_living
            }

        except Exception as e:
            print("Request failed:", e)
            return