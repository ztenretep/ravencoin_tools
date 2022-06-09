#!/usr/bin/python3
'''Get networkinfo from Ravencoin node.

Prerequisite: Ravencoin node must be running.
'''
# pylint: disable=invalid-name
# pylint: disable=broad-except
# pylint: disable=bare-except

# Import the Python modules.
import sys
import ast
import simplejson as json
import ravencoin.rpc

# Try to create an instance of ravencoin.rpc.Proxy().
try:
    rvn = ravencoin.rpc.Proxy()
except Exception as err:
    print(str(err))
    sys.exit(1)

# Set the service.
SERVICE = "addnode"

# Set the node.
NODE = "<ravencoin_node_ip>"

# Usage: add|remove|onetry
ARG = "add"

# Try to add a node.
try:
    response = rvn.call(SERVICE, NODE, ARG)
    response_str = json.dumps(response, indent=4)
    print(response_str)
except Exception as err:
    try:
        err_json = ast.literal_eval(str(err))
        err_str = json.dumps(err_json, indent=4)
    except:
        err_str = str(err)
    finally:
        print(err_str)
