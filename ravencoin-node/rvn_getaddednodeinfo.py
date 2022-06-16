#!/usr/bin/python3
'''Get Ravencoin node info from Ravencoin node.

Prerequisites:
    1. python-ravencoinlib 0.2.2 must be installed.
    2. Ravencoin node must be running.
'''

# Import the Python modules.
import sys
import os
import ast
import simplejson as json
import ravencoin.rpc
import ravencoin.core
import ravenrpc

# Try to create an instance of ravencoin.rpc.Proxy().
try:
    rvn = ravencoin.rpc.Proxy()
except Exception as err:
    print(str(err))
    sys.exit(1)

# Set the command.
SERVICE = "getaddednodeinfo"

# Try to get networkinfo.
try:
    # Get node info.
    response = rvn.call(SERVICE)
    response = json.dumps(response, indent=4)
    print(response)
except Exception as err:
    # Evaluate error.
    try:
        err_json = ast.literal_eval(str(err))
        err_str = json.dumps(err_json, indent=4)
    except:
        err_str = str(err)
    finally:
        print(err_str)
