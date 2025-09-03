import json
import requests

from keys import torn_api_key


class Company():
    def __init__(self, company_id: int, selections: str = ""):
        """
        The init function will initialise using:
        1. Company ID
        2. Selections (optional)

        Company ID must be supplied by the user.
        Selections are optional as the default non-selections returns most of the details.
        Selections can be specified as a comma-separated list of fields to include.

        Args:
            company_id (int): The Torn City company ID to query.
            selections (str, optional): Extra selections to include (default is "").
        """
        try:
            self.company_id = company_id
            self.selections = selections

            with open("endpoints_v1.json", "r") as f:
                self.endpoints = json.load(f)

            api_endpoint = self.endpoints["company"]
            url = api_endpoint.format(company_id=company_id, selections=selections, api_key=torn_api_key)

            response = requests.get(url)
            self.company_data = response.json()

        except Exception as e:
            print("Request failed:", e)

    def get_company_details(self):
        """
        Fetch the company details from the API.

        Returns:
            dict: The company details returned by the API:
                - "id" (int): Company ID
                - "type" (int): Company type
                - "type_name" (str): Company type name
                - "rating" (int): Company rating
                - "name" (str): Company name
                - "director" (int): Company director ID
                - "employees_hired" (int): Employees hired
                - "employees_capacity" (int): Employees capacity
                - "daily_income" (int): Daily income
                - "daily_customers" (int): Daily customers
                - "weekly_income" (int): Weekly income
                - "weekly_customers" (int): Weekly customers
                - "days_old" (int): Days old
                - "employees" (dict): Employees details
                    - (dict)
                        - "12345" (dict):
                            - "name" (str): Employee name
                            - "position" (str): Employee position
                            - "days_in_company" (int): Days in company
                            - "last_action" (dict): Last action details
                                - "status" (str): Last action status
                                - "timestamp" (int): Last action timestamp
                                - "relative" (str): Last action relative time
                            - "status" (dict): Employee status
                                - "description" (str): Employee status description
                                - "details" (str): Employee status details
                                - "state" (str): Employee status state
                                - "color" (str): Employee status color
                                - "until" (int): Employee status until timestamp
        """
        try:
            company_details = self.company_data.get("company", {})

            company_id = company_details.get("id", -1)
            company_type = company_details.get("company_type", -1)
            company_rating = company_details.get("rating", -1)
            company_index = {
                -1: "N/A",
                1: "Hair Salon",
                2: "Law Firm",
                3: "Flower Shop",
                4: "Car Dealership",
                5: "Clothing Store",
                6: "Gun Shop",
                7: "Game Shop",
                8: "Candle Shop",
                9: "Toy Shop",
                10: "Adult Novelty",
                11: "Cyber Cafe",
                12: "Grocery Store",
                13: "Theater",
                14: "Sweet Shop",
                15: "Cruise Line",
                16: "Television Network",
                17: "N/A",
                18: "Zoo",
                19: "Firework Stand",
                20: "Property Broker",
                21: "Furniture Store",
                22: "Gas Station",
                23: "Music Store",
                24: "Nightclub",
                25: "Pub",
                26: "Gents Strip Club",
                27: "Restaurant",
                28: "Oil Rig",
                29: "Fitness Center",
                30: "Mechanic Shop",
                31: "Amusement Park",
                32: "Lingerie Store",
                33: "Meat Warehouse",
                34: "Farm",
                35: "Software Corporation",
                36: "Ladies Strip Club",
                37: "Private Security Firm",
                38: "Mining Corporation",
                39: "Detective Agency",
                40: "Logistics Management"
            }
            company_type_name = company_index.get(company_type, "N/A")
            company_name = company_details.get("name", "N/A")
            company_director = company_details.get("director", -1)
            employees_hired = company_details.get("employees_hired", -1)
            employees_capacity = company_details.get("employees_capacity", -1)
            daily_income = company_details.get("daily_income", -1)
            daily_customers = company_details.get("daily_customers", -1)
            weekly_income = company_details.get("weekly_income", -1)
            weekly_customers = company_details.get("weekly_customers", -1)
            days_old = company_details.get("days_old", -1)
            employees = company_details.get("employees", {})

            return {
                "id": company_id,
                "type": company_type,
                "type_name": company_type_name,
                "rating": company_rating,
                "name": company_name,
                "director": company_director,
                "employees_hired": employees_hired,
                "employees_capacity": employees_capacity,
                "daily_income": daily_income,
                "daily_customers": daily_customers,
                "weekly_income": weekly_income,
                "weekly_customers": weekly_customers,
                "days_old": days_old,
                "employees": employees
            }
        
        except Exception as e:
            print("Request failed:", e)
            return
