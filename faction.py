import json
import requests

from keys import torn_api_key


def get_faction_details():
    try:
        with open("endpoints_v1.json", "r") as f:
            endpoints = json.load(f)

        # faction_id = input("Enter Faction ID: ")
        faction_id = 51042
        # selections = input("Enter selections (or leave blank): ")
        selections = ""

        api_endpoint = endpoints["faction"]
        url = api_endpoint.format(faction_id=faction_id, selections=selections, api_key=torn_api_key)

        response = requests.get(url)
        faction_data = response.json()

        faction_id = faction_data.get("ID", "N/A")
        faction_name = faction_data.get("name", "N/A")
        faction_tag = faction_data.get("tag", "N/A")
        faction_tag_image = faction_data.get("tag_image", "N/A")
        faction_leader = faction_data.get("leader", "N/A")
        faction_co_leader = faction_data.get("co-leader", "N/A")
        faction_respects = faction_data.get("respect", "N/A")
        faction_age = faction_data.get("age", "N/A")
        faction_capacity = faction_data.get("capacity", "N/A")
        faction_best_chain = faction_data.get("best_chain", "N/A")
        faction_territory_wars = faction_data.get("territory_wars", {})
        faction_raid_wars = faction_data.get("raid_wars", {})
        faction_peace = faction_data.get("peace", {})
        faction_rank = faction_data.get("rank", {})
        faction_ranked_wars = faction_data.get("ranked_wars", {})
        faction_members = faction_data.get("members", {})

        # print(faction_members)

        all_members = []
        for fmk in faction_members:
            all_members.append(f"{fmk} - {faction_members[fmk]['name']}")

        print(f"Faction ID    : {faction_id}")
        print(f"Faction Name  : {faction_name}")
        print(f"Respect       : {faction_respects}")
        print(f"Age           : {faction_age} days")
        print(f"Best Chain    : {faction_best_chain}")
        print(f"Rank          : {faction_rank['name']} - Division {faction_rank['division']}")
        print(f"Members Count : {len(faction_members)}")
        print(all_members)

    except Exception as e:
        print("Request failed:", e)
        return