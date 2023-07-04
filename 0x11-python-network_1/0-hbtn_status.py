#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urlliib.request

if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        ty = response.read()
        print("ty response")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
