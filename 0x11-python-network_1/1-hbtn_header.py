#!/usr/bin/python3
"""
     Python script that takes in a URL, sends a request to the URL and displays
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
