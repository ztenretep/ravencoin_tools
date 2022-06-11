#!/usr/bin/bash

# Set user and password.
USER="<rpcuser>"
PASSWORD="<rpcpassword>"

# Set service url.
URL="http://127.0.0.1:8766/"

# Set the request header.
HEADER="content-type: text/plain;"

# Set the request data.
DATA='{
       "jsonrpc": "1.0", "id":"curl", "method": "help", "params": []
      }'

# Get response from interface.
response=$(curl -s --user "${USER}":"${PASSWORD}" --data-binary "${DATA}" -H "${HEADER}" "${URL}")

# Print response to screen.
echo -e "${response}"

# Exit script without error.
exit 0
