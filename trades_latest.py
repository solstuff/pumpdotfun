import requests

LAMPORTS = 1e9
resp = requests.get("https://frontend-api.pump.fun/trades/latest").json()
sol_amount = resp["sol_amount"] / LAMPORTS
print(f"Event: ", "Buy" if resp["is_buy"] else "Sell")
print(f"Solana amount: ", sol_amount)
print(f"Ticker: {resp["symbol"]}")
print(f"User: {resp["user"]}")