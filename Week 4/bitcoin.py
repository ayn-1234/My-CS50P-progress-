import requests
import sys
import json


def main():
    bitcoin()



def bitcoin():

        try:
            if len(sys.argv) == 2:
                  n = float(sys.argv[1])
            else:
                 sys.exit("Missing command-line argument")

        except ValueError:
            sys.exit("Command-line argument is not a number")

        try:
            bitcoin_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            bitcoin_json = bitcoin_api.json()
            bitcoin_rate = bitcoin_json["bpi"]["USD"]["rate_float"]
            usdToBtc = n * bitcoin_rate
            print(f"${usdToBtc:,.4f}")


        except requests.RequestException:
            sys.exit("Sorry the request couldn't be taken. Try Again!")




main()

#Completed Assingment
#Alhamdulliah
