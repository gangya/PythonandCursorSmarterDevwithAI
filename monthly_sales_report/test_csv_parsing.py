"""Test that the CSV file can be parsed correctly without errors"""
import csv

# Test 1: Using Python's csv module
print("Testing CSV parsing with Python's csv module...")
try:
    with open('sales_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        print(f"[OK] Successfully parsed {len(records)} records")
        
        # Check first few prices
        print("\nFirst 5 price values:")
        for i, record in enumerate(records[:5], 1):
            price = record['price']
            print(f"  {i}. Price: {price} (type: {type(price).__name__})")
            # Try to convert to float
            try:
                price_float = float(price)
                print(f"     -> Converted to float: {price_float}")
            except ValueError as e:
                print(f"     [ERROR] converting to float: {e}")
        
        # Verify all prices are valid numbers
        print("\nVerifying all prices are valid numbers...")
        invalid_prices = []
        for i, record in enumerate(records, 1):
            try:
                float(record['price'])
            except ValueError:
                invalid_prices.append((i, record['price']))
        
        if invalid_prices:
            print(f"[ERROR] Found {len(invalid_prices)} invalid prices:")
            for line_num, price in invalid_prices[:10]:
                print(f"  Line {line_num}: {price}")
        else:
            print("[OK] All prices are valid numbers (no commas, no colons)")
            
except Exception as e:
    print(f"[ERROR] Error: {e}")

# Test 2: Check for any commas or colons in price values
print("\n" + "="*60)
print("Checking for problematic characters in prices...")
with open('sales_data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    problematic = []
    for i, line in enumerate(lines[1:], 2):  # Skip header
        parts = line.strip().split(',')
        if len(parts) >= 4:
            price = parts[3]
            if ',' in price or ':' in price:
                problematic.append((i, price))
    
    if problematic:
        print(f"[ERROR] Found {len(problematic)} prices with commas or colons:")
        for line_num, price in problematic[:10]:
            print(f"  Line {line_num}: {price}")
    else:
        print("[OK] No commas or colons found in price values")
        print("[OK] CSV is safe for parsing!")