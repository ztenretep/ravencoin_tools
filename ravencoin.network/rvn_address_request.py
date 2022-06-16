!/usr/bin/python3
'''Get RVN address info.
'''

# Import the Python modules.
import requests
import json

# Set Ravencoin address.
RVN_ADDRESS = "<rvn_address>"

# Assemble URL.
URL = "https://ravencoin.network/api/addr/" + RVN_ADDRESS

# Define request headers.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept-Language': 'en-US;q=0.3,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# Get the response.
response = requests.get(URL, headers=headers)

# Create JSON data.
response = response.json()

# Create formated string data.
resp = json.dumps(response, indent=2)

# Print formated result.
print(resp)
