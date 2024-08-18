import requests

LAMPORTS = 1_000_000_000

address = input("Enter Address: ")
# Entering address via console - limit is how many returned (Max 50) | offset will remove most recent for query
resp = requests.get("https://frontend-api.pump.fun/trades/%s?limit=100&offset=0" % (address)).json()

sells = 0; buys = 0
sol_sold = 0; sol_bought = 0

for transaction in resp:
	if transaction["is_buy"]:
		buys += 1; sol_bought += transaction["sol_amount"]
	else:
		sells += 1; sol_sold += transaction["sol_amount"]

sol_sold = sol_sold / LAMPORTS; sol_bought = sol_bought / LAMPORTS
total_sol_traded = sol_sold + sol_bought

print("\nLast 100 transaction trade stats for " + address[0:9])
print(f"{sol_bought:,.0f} SOL in {buys} buys")
print(f"{sol_sold:,.0f} SOL in {sells} sells")
print(f"Total: {total_sol_traded:,.0f}")