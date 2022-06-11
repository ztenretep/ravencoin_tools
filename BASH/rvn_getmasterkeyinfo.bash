#!/usr/bin/bash
#
# Description: Get Master Key info.
#
# rpc-user and rpc-password have to be set in the raven.conf.

# Set user and password.
USER="<rpc-user>"
PASSWORD="<rpc-password>"

# Set service url.
URL="http://127.0.0.1:8766/"

# Set service.
SERVICE="getmasterkeyinfo"

# Set the request header.
HEADER="content-type: text/plain;"

# Set the request data.
DATA="{
       \"jsonrpc\": \"1.0\", \"id\":\"curlreq\", \"method\": \"${SERVICE}\", \"params\": []
      }"

# Get response from interface.
response=$(curl -s --user "${USER}":"${PASSWORD}" --data-binary "${DATA}" -H "${HEADER}" "${URL}")

# Print response to screen.
echo -e "${response}" | jq

# Exit script without error.
exit 0
