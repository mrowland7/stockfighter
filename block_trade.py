# Buy 100,000 shares of YHG for account BFS81793627.
import requests
import json
import ssl
from time import sleep

api_key = '75d1b80513a170217fcd0bdcbd9f9bc283ee8600'
heartbeat_url = 'https://api.stockfighter.io/ob/api/heartbeat'
REQUIRED_SHARES = 100000
account = 'BT62002076'
stock = 'OTGU'
venue = 'NYGMEX'
num_transactions = 1000

def transact(url, direction, shares, price):
    r = requests.post(url, data = json.dumps({
        'account': account,
        'venue': venue,
        'stock': stock,
        'price': int(price * 100),
        'qty': int(shares),
        'direction': direction,
        'orderType': 'fill-or-kill',
        }),
        headers = {
            'X-Starfighter-Authorization': api_key
            }
        )
    response = r.json()
    if not response['ok']:
        print 'Response not ok:', response
    print 'Was order filled?', response['totalFilled']
    print response

def main():
    response = requests.get(heartbeat_url)
    if not response.json()['ok']:
        print 'server is down, quitting'

    print 'Server is up. Starting...'

    api = 'https://api.stockfighter.io/ob/api/venues/' + venue + '/stocks/' + stock + '/orders'
    print "transacting from", api
    auto_mode = False
    while True:
        direction = raw_input("Buy, sell, r, auto: ")
        if direction == "rpt" or direction == "r":
            transact(api, old_direction, num_shares, price)
            continue
        num_shares = float(raw_input("How many shares? "))
        price = float(raw_input("What target price? "))
        old_direction = direction
        if direction == "buy":
            print "buying"
            transact(api, "buy", num_shares, price)
        elif direction == "sell":
            print "selling"
            transact(api, "sell", num_shares, price)
        else:
            print "staying put"

if __name__ == '__main__':
    main()
