"""
Generate synthetic sales data with columns: date, product, quantity, price
"""
import csv
import random
from datetime import datetime, timedelta

# Product list
products = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "Headphones",
    "Webcam", "USB Drive", "External Hard Drive", "Tablet", "Smartphone",
    "Printer", "Scanner", "Router", "Cable", "Adapter",
    "Charger", "Battery", "Case", "Stand", "Speaker"
]

# Generate data for the past 12 months
start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()

# Generate sales records
sales_data = []
for _ in range(1000):  # Generate 1000 sales records
    # Random date within the past year
    random_days = random.randint(0, 365)
    date = start_date + timedelta(days=random_days)
    
    # Random product
    product = random.choice(products)
    
    # Random quantity (1-10)
    quantity = random.randint(1, 10)
    
    # Price based on product (with some variation)
    base_prices = {
        "Laptop": 800, "Mouse": 25, "Keyboard": 50, "Monitor": 200, "Headphones": 80,
        "Webcam": 60, "USB Drive": 15, "External Hard Drive": 100, "Tablet": 400,
        "Smartphone": 600, "Printer": 150, "Scanner": 120, "Router": 80, "Cable": 10,
        "Adapter": 20, "Charger": 25, "Battery": 30, "Case": 40, "Stand": 35, "Speaker": 70
    }
    base_price = base_prices.get(product, 50)
    # Add some price variation (±20%)
    price = round(base_price * random.uniform(0.8, 1.2), 2)
    
    sales_data.append({
        'date': date.strftime('%Y-%m-%d'),
        'product': product,
        'quantity': quantity,
        'price': price  # Keep as float, will be formatted during CSV write
    })

# Sort by date
sales_data.sort(key=lambda x: x['date'])

# Write to CSV
# Ensure prices are written as plain numbers (no formatting, no thousand separators)
# This prevents CSV parsing errors from commas or colons in numbers
filename = 'monthly_sales_report/sales_data.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['date', 'product', 'quantity', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    
    writer.writeheader()
    for sale in sales_data:
        # Format price as plain numeric string (no thousand separators, period as decimal)
        # This ensures clean CSV parsing - no commas or colons in numbers
        price_float = float(sale['price'])
        sale['price'] = f"{price_float:.2f}"
        writer.writerow(sale)

print(f"Generated {len(sales_data)} sales records")
print(f"Data saved to: {filename}")
print(f"\nFirst 5 records:")
for i, sale in enumerate(sales_data[:5], 1):
    print(f"  {i}. {sale}")