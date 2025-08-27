import json
import time
import requests

from keys import torn_api_key
from datetime import datetime, timezone
from faction import get_faction_details


def main():
    get_faction_details()


if __name__ == "__main__":
    main()