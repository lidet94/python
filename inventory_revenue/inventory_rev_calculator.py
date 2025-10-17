inventory = [
    {"item": "Shoes", "price": 23, "quantity": 2},
    {"item": "Jumper", "price": 14, "quantity": 1},
    {"item": "T-shirt", "price": 5, "quantity": 2},
]

# Calculate revenue
revenue_list = []
for item in inventory:
    total = item["price"] * item["quantity"]
    revenue_list.append({"item": item["item"], "revenue": total})

# Sort descending by revenue
sorted_revenue = sorted(revenue_list, key=lambda u: u["revenue"], reverse=True)

# Print results
print("Inventory revenue (high to low):")
for r in sorted_revenue:
    print(f"{r['item']}: £{r['revenue']}")
