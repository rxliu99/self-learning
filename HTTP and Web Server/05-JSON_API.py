#!/usr/bin/env python3
#
# Using a JSON API: Client for the UINames.com service.
# Example output:
#   My name is Tyler Hudson and the PIN on my card is 4840.
#
# NOTE: UINames.com does not exist anymore, so the code will raise an exception.


# requests is a Python library for sending requests to web servers 
# and interpreting the responses
import requests

def SampleRecord():
    # Send a GET request to server.
    r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)
    
    # Decode JSON from the response object.
    j = r.json()
    
    return "My name is {} {} and the PIN on my card is {}.".format(
        j["name"],
        j["surname"],
        j["credit_card"]["pin"]
    )

if __name__ == '__main__':
    print(SampleRecord())
