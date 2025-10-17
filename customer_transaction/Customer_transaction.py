customers = [
    {"name": "Maya", "transactions": [300, -50, 100, -20, 50]},
    {"name": "Eli", "transactions": [100, -120, 50, -10]},
    {"name": "Zara", "transactions": [500, 200, -150, 100]},
    {"name": "Ben", "transactions": [-50, -30, -20]},
    {"name": "Noah", "transactions": [400, -200, 50, 50]},
]

# Calculate each customer's net balance
totals = []
for c in customers:
    net = sum(c["transactions"])
    if net >= 0:
        totals.append({"name": c["name"], "net_balance": net})

# Sort descending by balance
sorted_customers = sorted(totals, key=lambda u: u["net_balance"], reverse=True)

# Output
print("Customer balances (positive only):")
for c in sorted_customers:
    print(f"{c['name']}: £{c['net_balance']}")
