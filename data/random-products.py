import random
import string
import uuid
from datetime import datetime, timedelta
import csv

# Helper functions
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_price():
    return round(random.uniform(1.0, 50.0), 2)

def random_quantity():
    return random.randint(1, 100)

def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Grocery categories, products, and brands
categories = {
    "Beverages": ["Coca-Cola", "Pepsi", "Orange Juice", "Apple Juice", "Water", "Milk", "Gatorade", "Red Bull"],
    "Snacks": ["Lays Chips", "Doritos", "Oreos", "Snickers", "Granola Bar", "Popcorn", "Pretzels", "Trail Mix"],
    "Produce": ["Bananas", "Apples", "Carrots", "Lettuce", "Tomatoes", "Cucumbers", "Strawberries", "Avocados"],
    "Bakery": ["White Bread", "Whole Wheat Bread", "Bagels", "Croissants", "Donuts", "Cakes", "Muffins"],
    "Frozen Foods": ["Frozen Pizza", "Frozen Vegetables", "Ice Cream", "Frozen Meals", "Frozen Chicken", "Fish Sticks"],
    "Meat": ["Chicken Breast", "Ground Beef", "Pork Chops", "Steak", "Bacon", "Sausage"],
    "Dairy": ["Cheddar Cheese", "Yogurt", "Butter", "Eggs", "Cream Cheese", "Sour Cream"],
    "Canned Goods": ["Tomato Soup", "Canned Corn", "Canned Beans", "Canned Tuna", "Canned Tomatoes"],
    "Pasta & Grains": ["Spaghetti", "Brown Rice", "Quinoa", "Macaroni", "Couscous", "Oats", "Barley"],
}

product_descriptions = {
    "Beverages": "Refreshing and perfect for any occasion.",
    "Snacks": "Delicious and crunchy snack for any time of the day.",
    "Produce": "Fresh and organic from the farm.",
    "Bakery": "Baked fresh daily.",
    "Frozen Foods": "Convenient and ready-to-eat frozen meals.",
    "Meat": "High-quality and freshly cut.",
    "Dairy": "Rich in calcium and fresh.",
    "Canned Goods": "Long-lasting pantry essentials.",
    "Pasta & Grains": "Great for hearty meals."
}

# Storage types and departments
storage_types = ["Bulk", "Pallet Rack", "Shelf", "Cold Storage", "Bin"]
departments = ["Frozen", "Dry", "Standard"]

# UOM (Unit of Measure)
uoms = ["Unit", "Case", "Box", "Pack", "Pallet"]

# Subcategories for products
subcategories = {
    "Beverages": ["Soft Drinks", "Juices", "Water", "Energy Drinks"],
    "Snacks": ["Chips", "Cookies", "Candy", "Nuts"],
    "Produce": ["Fruits", "Vegetables", "Herbs", "Berries"],
    "Bakery": ["Bread", "Pastries", "Cakes", "Muffins"],
    "Frozen Foods": ["Pizza", "Vegetables", "Desserts", "Prepared Meals"],
    "Meat": ["Poultry", "Beef", "Pork", "Fish"],
    "Dairy": ["Cheese", "Milk Products", "Butter", "Yogurt"],
    "Canned Goods": ["Soups", "Vegetables", "Fish", "Tomatoes"],
    "Pasta & Grains": ["Pasta", "Rice", "Grains", "Cereals"]
}

# Generate random grocery products with additional fields
def generate_grocery_data(num_products=1000):
    vendors = []
    products = []
    product_profiles = []
    purchases = []
    sales = []
    expenses = []
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 1, 1)

    for i in range(1, num_products + 1):
        productId = str(uuid.uuid4())
        vendor_id = str(uuid.uuid4())

        # Select random category and product
        category = random.choice(list(categories.keys()))
        product_name = random.choice(categories[category])
        product_desc = product_descriptions[category]

        # Randomly select unique subcategories and department
        subcategory_choices = random.sample(subcategories[category], 3)  # Ensure unique subcategories
        subcategory1, subcategory2, subcategory3 = subcategory_choices[0], subcategory_choices[1], subcategory_choices[2]
        department = random.choice(departments)
        storage_type = random.choice(storage_types)
        inv_uom = random.choice(uoms)
        purchase_uom = random.choice(uoms)
        sales_uom = random.choice(uoms)

        # Generate random vendor data
        vendors.append({
            "id": vendor_id,
            "name": f"Vendor {random.choice(string.ascii_uppercase)}{random.randint(1, 100)}",
            "productNumber": f"PN{i}",
            "type": "Standard",
            "leadTime": random.randint(1, 10),
            "contact": f"Contact {random_string(5)}",
            "phone": f"+1-800-{random.randint(1000, 9999)}",
            "email": f"vendor{random_string(5)}@grocery.com",
            "countryOfOrigin": random.choice(["USA", "Canada", "Mexico", "Brazil"]),
            "buyer": f"Buyer {random.choice(string.ascii_uppercase)}",
            "agent": f"Agent {random.choice(string.ascii_uppercase)}"
        })
        
        # Generate random product data
        products.append({
            "productId": productId,
            "product_name": product_name,
            "product_desc": product_desc,
            "gtin": ''.join(random.choices(string.digits, k=12)),
            "product_subtype": "Standard",
            "buyer_group": f"Buyer Group {random.choice(string.ascii_uppercase)}",
            "inv_uom": inv_uom,
            "purchase_uom": purchase_uom,
            "sales_uom": sales_uom,
            "primary_category": category,
            "subcategory1": subcategory1,
            "subcategory2": subcategory2,
            "subcategory3": subcategory3,
            "department": department,
            "product_sales_tax_group": "Standard",
            "product_purchase_tax_group": "Standard",
            "catchweight_flag": random.choice([True, False]),
            "product_model_group": f"Model Group {random.choice(string.ascii_uppercase)}",
            "product_group": f"Group {random.choice(string.ascii_uppercase)}",
            "storage_type": storage_type,
            "vendor_id": vendor_id,
            "multiple_vendor_flag": random.choice([True, False]),
            "purchase_price": random_price(),
            "sales_price": random_price(),
            "inv_price": random_price()
        })

        # Generate random product profile data
        product_profiles.append({
            "id": i,
            "productId": productId,
            "productLength": random.uniform(5, 50),
            "productWidth": random.uniform(5, 50),
            "productHeight": random.uniform(5, 50),
            "caseLength": random.uniform(10, 100),
            "caseWidth": random.uniform(10, 100),
            "productCubicFt": random.uniform(1, 5),
            "caseCubicFt": random.uniform(1, 5),
            "ti": random.randint(1, 5),
            "hi": random.randint(1, 5),
            "tiersPerPallet": random.randint(1, 10)
        })

        # Generate random purchase data
        purchases.append({
            "purchaseId": str(uuid.uuid4()),
            "productId": productId,
            "timestamp": random_date(start_date, end_date),
            "quantity": random_quantity(),
            "unitCost": random_price(),
            "landedCost": random_price(),
            "totalCost": random_price()
        })

        # Generate random sales data
        sales.append({
            "saleId": str(uuid.uuid4()),
            "productId": productId,
            "timestamp": random_date(start_date, end_date),
            "quantity": random_quantity(),
            "unitPrice": random_price(),
            "totalAmount": random_price()
        })

        # Generate random expense data
        expenses.append({
            "expenseId": str(uuid.uuid4()),
            "category": random.choice(["Operating", "Administrative", "Maintenance"]),
            "amount": random_price(),
            "timestamp": random_date(start_date, end_date)
        })

    return vendors, products, product_profiles, purchases, sales, expenses, storage_types

# Function to write a list of dictionaries to a CSV file
def write_to_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Generate 1000 products and their related data
vendors, products, product_profiles, purchases, sales, expenses, storage_types = generate_grocery_data(1000)

# Write the data to CSV files
write_to_csv('vendors.csv', vendors, vendors[0].keys())
write_to_csv('products.csv', products, products[0].keys())
write_to_csv('product_profiles.csv', product_profiles, product_profiles[0].keys())
write_to_csv('purchases.csv', purchases, purchases[0].keys())
write_to_csv('sales.csv', sales, sales[0].keys())
write_to_csv('expenses.csv', expenses, expenses[0].keys())

print("CSV files generated successfully.")
