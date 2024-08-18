import requests

address = input("Enter Address: ")
# Entering address via console - limit is how many returned (Max 50) | offset will remove most recent tokens for count
resp = requests.get("https://frontend-api.pump.fun/coins/user-created-coins/%s?limit=50&offset=1&includeNsfw=true" % (address)).json()

print("")
bad_coins = 0; decent_tokens = 0
for coin in resp:
	if coin["usd_market_cap"] >= 10000:
		print(f"Over $10,000 market cap! {coin["mint"]}"); decent_tokens += 1
	elif coin["raydium_pool"]:
		print(f"Oh my god hit ray!! {coin["mint"]}"); decent_tokens += 1
	else: bad_coins += 1

print(f"\n{address[0:7]} Has created {bad_coins} useless tokens & {decent_tokens} alright tokens")