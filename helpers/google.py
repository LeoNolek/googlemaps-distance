from .api import Api
import math
import os
from dotenv import load_dotenv
load_dotenv()

routes_url = os.getenv("ROUTES_API_URL")
coordinates_url = os.getenv("COORDINATES_API_URL")


class GoogleApi:
    def __init__(self, token):
        self.route_api = Api(routes_url)
        self.coordinates_api = Api(coordinates_url)
        self.token = token
        pass

    def get_coordinates(self, address):
        endpoint = "geocode/json"
        headers = { 
            "X-Goog-Api-Key": self.token,
            "Content-Type": "application/json"
        }
        params = {
            "address": address,
            "key": self.token
        }
        response = self.coordinates_api.get(endpoint=endpoint, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data and 'results' in data and len(data['results']) > 0:
                coords = data['results'][0]['geometry']['location']
                return coords['lat'], coords['lng']
            else:
                print("No results found")
                return None
        else:
            print(f"Error: {response.status_code}")
            return None

    def calculate_straight_line_distance(self, origin, destination):
        """
        Calculate the straight-line distance (Haversine distance) between two points.
        :param origin_coords: Tuple of (latitude, longitude) for the origin.
        :param destination_coords: Tuple of (latitude, longitude) for the destination.
        :return: Distance in meters.
        """
        # Radius of the Earth in meters
        R = 6371000

        # Convert latitude and longitude from degrees to radians
        lat1, lon1 = map(math.radians, self.get_coordinates(origin))
        lat2, lon2 = map(math.radians, self.get_coordinates(destination))

        # Differences in coordinates
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        # Haversine formula
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distance in meters
        distance = R * c
        print(f"Straight-line distance: {distance} meters")
        return round(distance/1000,3)


    def calculate_route_distance(self, origin, destination):
        endpoint = "distanceMatrix/v2:computeRouteMatrix"
        headers = { 
            "X-Goog-Api-Key": self.token,
            "Content-Type": "application/json",
            "X-Goog-FieldMask": "distanceMeters"
        }
        data = {
            "origins": [{
                "waypoint": {
                    "address": origin
                    }
                }
            ],
            "destinations": [{
                "waypoint": {
                    "address": destination
                    }   
                }
            ]
        }
        response = self.route_api.post(endpoint=endpoint, json=data, headers=headers)
        distance = response.json()[0]['distanceMeters']
        print(f"Route distance: {distance} meters")
        return round(distance/1000,3)





