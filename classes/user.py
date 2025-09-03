import json
import requests

from keys import torn_api_key


class Company():
    def __init__(self, user_id: int, selections: str = ""):
        """
        The init function will initialise using:
        1. User ID
        2. Selections (optional)

        User ID must be supplied by the user.
        Selections are optional as the default non-selections returns most of the details.
        Selections can be specified as a comma-separated list of fields to include.

        Args:
            user_id (int): The Torn City user ID to query.
            selections (str, optional): Extra selections to include (default is "").
        """
        try:
            self.user_id = user_id
            self.selections = selections

            with open("endpoints_v1.json", "r") as f:
                self.endpoints = json.load(f)

            api_endpoint = self.endpoints["user"]
            url = api_endpoint.format(user_id=user_id, selections=selections, api_key=torn_api_key)

            response = requests.get(url)
            self.user_data = response.json()

        except Exception as e:
            print("Request failed:", e)

    def get_user_details(self):
        """
        Fetch the company details from the API.

        Returns:
            
        """
        
