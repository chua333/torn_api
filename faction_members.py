import time
import requests

from keys import torn_api
from datetime import datetime, timezone

API_KEY = torn_api
FACTION_ID = 50433
URL = f"https://api.torn.com/v2/faction/{FACTION_ID}/members?striptags=true&key={API_KEY}"


def format_mmss(hosp_until):
    dt_utc = datetime.fromtimestamp(hosp_until, timezone.utc)
    now_utc = datetime.now(timezone.utc)

    delta = dt_utc - now_utc
    total_seconds = int(delta.total_seconds())

    if total_seconds <= 0:
        print("Hospital time has expired or is in the past.")
    else:
        m, s = divmod(total_seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        parts = []
        if d: parts.append(f"{d}d")
        if d or h: parts.append(f"{h}h")
        if d or h or m: parts.append(f"{m}m")
        parts.append(f"{s}s")
        print("Remaining hospital time:", " ".join(parts))
    


def get_faction_members():
    try:
        print()
        response = requests.get(URL)
        data = response.json()

        server_ts = int(data.get('timestamp', time.time()))

        count_sa = 0
        attack_prep = []

        if "members" in data:
            members_data = data["members"]
            for member in members_data:
                member_name = member.get('name', 'Unknown')
                member_id = member.get('id', 'Unknown')
                member_status = member.get('status', {})
                member_description = member_status.get('description', 'No description')

                if "south africa" in member_description.lower():
                    count_sa += 1
                    print(f"Member: {member_name} (ID: {member_id}) - {member_description}")

                    hosp_until = member_status.get("until", 0)
                    if isinstance(hosp_until, int):
                        if hosp_until > 0 or hosp_until is not None:
                            formatted_time = format_mmss(hosp_until)
                            print(f"Hospital Time: {formatted_time}")
                        else:
                            print(f"Hospital Time: Not in hospital")
                        
                        if "hospital" in member_description.lower() and hosp_until > server_ts:
                            attack_prep.append(member_name)
                    else:
                        print(f"Hospital Time: Not in hospital")

                    API_v1 = f"https://api.torn.com/user/{member_id}?selections=&key={API_KEY}"
                    response_v1 = requests.get(API_v1)
                    data_v1 = response_v1.json()

                    last_action_data = data_v1.get('last_action', 'N/A')
                    if last_action_data != 'N/A':
                        print(f"Status: {last_action_data['status']}")
                        print(f"Relative: {last_action_data['relative']}")
                        print()

            print(f"Total members from South Africa: {count_sa}")
            print(f"People to attack: {', '.join(attack_prep)}" if attack_prep else "No members to attack.")
        else:
            print("Error or missing members in API response:", data)
            return []
    except Exception as e:
        print("Request failed:", e)
        return []

def main():
    while True:
        members = get_faction_members()
        if members:
            print(", ".join(members))
        time.sleep(3)

if __name__ == "__main__":
    main()

get_faction_members()
