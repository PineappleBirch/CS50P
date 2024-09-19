import json
import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()

answer = n * o["bpi"]["USD"]["rate_float"]

print(f"${answer:,.4f}")
