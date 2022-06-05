#!/usr/bin/env python3

import os
import sys
import requests
#import pandas as pd

base_url = "https://apiservice.borsdata.se/v1/"
auth_key = os.environ.get('BORSDATA_AUTH_KEY')

if auth_key == None:
    sys.exit("Set BORSDATA_AUTH_KEY environment variable")

params = {
    "authKey": auth_key,
    "maxCount": 20,
}

def call_api(url, params):
    response = requests.get(url, params)

    if response.status_code != 200:
        sys.exit(f"Error calling API. Return code {response.status_code}")

    return response.json()

json_data = call_api(base_url + "branches", params)

print(f"{json_data}")
