#!/usr/bin/python3
'''Get RVN address info.

Ref.: https://rvn.cryptoscope.io/api/
'''

# Im,port the Python modules.
import requests
import json

# Set Ravencoin address.
RVN_ADDRESS = "<rvn_address>"

# Assemble URL.
URL = "https://rvn.cryptoscope.io/api/getaddress/?address=" + RVN_ADDRESS

# Get the response.
response = requests.get(URL)

# Create JSON data.
response = response.json()

# Create formated string data.
resp = json.dumps(response, indent=2)

# Print formated result.
print(resp)

