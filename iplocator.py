"""
This Script will allow you to check a geolocation of an IP address

params : -i ip [ip ... ]

Author : David Gitman
"""

import requests
import argparse
import os

# This is the API url
url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
api_key = os.environ.get('api_key')
# Set up headers for API call
headers = {
    'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
    'x-rapidapi-key': api_key
}
# Get Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ips', nargs="+", action='extend', dest='ip', type=str, help='write an IP address',
                    required=True)
args = parser.parse_args()

# Print geolocation for each IP in the Arguments
for ip in args.ip:
    print(ip)

    # Request geolocation from API
    querystring = {"ip": ip}
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Print geolocation results
    try:
        response = response.json()
        city = response["city"]
        region = response["region"]
        country = response["country"]
        print("City: " + city)
        print("Region: " + region)
        print("Country: " + country)
        print()

    # Handle Exception
    except Exception:
        print("invalid IP address: " + querystring["ip"])
        print()


def py():
    return None
