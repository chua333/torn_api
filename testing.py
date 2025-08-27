import json

# Load endpoint templates from file
with open("endpoints.json", "r") as f:
    endpoints = json.load(f)

def build_url(endpoint_name, **kwargs):
    """Fill placeholders in endpoint template with dynamic values."""
    template = endpoints[endpoint_name]
    print(f"Template before formatting: {template}")
    return template.format(**kwargs)

# Example usage
api_key = "E09xjRZDl7sytPzS"

# Get faction detail
url = build_url("faction", faction = 'haha', faction_id=51042, selections="", api_key=api_key)
print(url)
# -> https://api.torn.com/faction/51042?selections=&key=E09xjRZDl7sytPzS
