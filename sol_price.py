import requests

#sol_price = requests.get("https://frontend-api.pump.fun/sol-price").json()["solPrice"]
#print()
print(f"${requests.get("https://frontend-api.pump.fun/sol-price").json()["solPrice"]}")