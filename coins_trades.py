import requests
from time import sleep

latest_mints = []

while True:
	resp = requests.get("https://frontend-api.pump.fun/coins/latest").json()
	if resp["mint"] in latest_mints:
		continue
	elif len(latest_mints) >= 5:
		latest_mints.clear()
	else: print(f"\nNew Mint!\n{resp["mint"]}\nCreator: {resp["creator"]}"); latest_mints.append(resp["mint"])
	sleep(2)