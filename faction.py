import json
import requests

from keys import torn_api_key


class Faction:
    def __init__(self, faction_id: int, selections: str = ""):
        """
        The init function will initialise using:
        1. Faction ID
        2. Selections (optional)

        Faction ID must be supplied by the user.
        Selections are optional as the default non-selections returns most of the details.
        Selections can be specified as a comma-separated list of fields to include.

        Args:
            faction_id (int): The Torn City faction ID to query.
            selections (str, optional): Extra selections to include (default is "").
        """
        try:
            self.faction_id = faction_id
            self.selections = selections
            
            with open("endpoints_v1.json", "r") as f:
                self.endpoints = json.load(f)

            api_endpoint = self.endpoints["faction"]
            url = api_endpoint.format(faction_id=faction_id, selections=selections, api_key=torn_api_key)

            response = requests.get(url)
            self.faction_data = response.json()

        except Exception as e:
            print("Request failed:", e)

    def get_faction_members(self):
        """
        Get a dictionary of faction members.
        Example: {"12345": "Player 1", "23245": "Player 2"}

        Returns:
            dict: A dictionary mapping member IDs to their names:
                - "ID" (str): Player ID
                - "Name" (str): Player Name

        """
        try:
            faction_members = self.faction_data.get("members", {})

            all_members = {}

            for member_id in faction_members:
                all_members[member_id] = faction_members[member_id]['name']

            return all_members

        except Exception as e:
            print("Request failed:", e)
            return

    def get_faction_ranks(self):
        """
        Get a dictionary of faction ranks.

        Returns:
            dict: A dictionary mapping the details of faction ranks:
                - "level" (int): Rank Level
                - "name" (str): Rank Name
                - "division" (int): Rank Division
                - "position" (int): Rank Position
                - "wins" (int): Rank Wins

        """
        try:
            faction_ranks = self.faction_data.get("rank", {})

            return faction_ranks

        except Exception as e:
            print("Request failed:", e)
            return

    def get_faction_ranked_wars(self):
        """
        Get detailed information about ranked wars in the faction.

        Returns:
            dict: A dictionary of dictionary mapping all current ranked wars:
                - "12456" (dict): Ranked War ID
                    - "factions" (dict): A dictionary mapping faction's ID
                        - "12456" (dict): Faction ID
                            - "name" (str): Faction Name
                            - "score" (int): Faction Score
                            - "chain" (int): Faction Chain
                    - "wars" (dict): A dictionary mapping details of the war
                        - "start" (int): War Start Time Stamp
                        - "score" (int): War Score
                        - "chain" (int): War Chain
        """

        try:
            faction_ranked_wars = self.faction_data.get("ranked_wars", {})

            return faction_ranked_wars
        
        except Exception as e:
            print("Request failed:", e)
            return

    def get_faction_wars_and_peaces(self):
        """
        Get detailed information about a faction's normal war and peace treaty.

        Returns:
            dict: A dictionary mapping the details of the faction's wars and peace treaties:
            - "territory_wars" (list): contains a list of dicts the details of the territory wars
                - (dict)
                    - "territory_war_id" (int): Territory War ID
                    - "territory" (str): Territory Name
                    - "assaulting_faction" (int): Assaulting Faction ID
                    - "defending_faction" (int): Defending Faction ID
                    - "score" (int): War Score
                    - "required_score" (int): Required Score
                    - "start_time" (int): War Start Time Stamp
                    - "end_time" (int): War End Time Stamp
                    - "assaulters" (list): A list of assaulters in the war
                    - "defenders" (list): A list of defenders in the war
            - "raid_wars" (list): a list of dicts on the details of each raids
                - (dict)
                    - "raiding_faction" (int): Raiding Faction ID
                    - "defending_faction" (int): Defending Faction ID
                    - "raider_score" (int): Raider Score
                    - "defender_score" (int): Defender Score
                    - "start_time" (int): Raid Start Time Stamp
            - "peace" (dict): contains the ids and the time until the treaty ends
                - "12345" (int): Date until treaties ends
        """

        try:
            faction_territory_wars = self.faction_data.get("territory_wars", {})
            faction_raid_wars = self.faction_data.get("raid_wars", {})
            faction_peace = self.faction_data.get("peace", {})

            return {
                "territory_wars": faction_territory_wars,
                "raid_wars": faction_raid_wars,
                "peace": faction_peace
            }
        
        except Exception as e:
            print("Request failed:", e)
            return

    def get_faction_details(self):
        """
        Get detailed information about a faction.

        Args:
            faction_id (int): The Torn City faction ID to query.
            selections (str, optional): Extra selections to include (default is "").

        Returns:
            dict: A dictionary containing faction details, including keys such as:
                - "ID" (int): Faction ID
                - "name" (str): Faction name
                - "tag" (str): Faction tag
                - "tag_image" (str): Faction tag image
                - "leader" (str): Faction leader
                - "co-leader" (str): Faction co-leader
                - "respect" (int): Current faction respect
                - "age" (int): Faction age in days
                - "capacity" (int): Faction capacity
                - "best_chain" (int): Faction best chain
        """
        try:
            faction_id = self.faction_data.get("ID", "N/A")
            faction_name = self.faction_data.get("name", "N/A")
            faction_tag = self.faction_data.get("tag", "N/A")
            faction_tag_image = self.faction_data.get("tag_image", "N/A")
            faction_leader = self.faction_data.get("leader", "N/A")
            faction_co_leader = self.faction_data.get("co-leader", "N/A")
            faction_respects = self.faction_data.get("respect", "N/A")
            faction_age = self.faction_data.get("age", "N/A")
            faction_capacity = self.faction_data.get("capacity", "N/A")
            faction_best_chain = self.faction_data.get("best_chain", "N/A")

            faction_details = {
                "ID": faction_id,
                "name": faction_name,
                "tag": faction_tag,
                "tag_image": faction_tag_image,
                "leader": faction_leader,
                "co-leader": faction_co_leader,
                "respect": faction_respects,
                "age": faction_age,
                "capacity": faction_capacity,
                "best_chain": faction_best_chain
            }

            return faction_details

        except Exception as e:
            print("Request failed:", e)
            return
        