import json
import psycopg2
from psycopg2 import sql

# Database connection settings (update with your database credentials)
db_config = {
    'dbname': 'luxe_carats',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

# Mapping the JSON keys to the columns in your diamonds table
json_to_db_mapping = {
    "Lot #": "lot_number",
    "Shape": "shape",
    "Color": "color",
    "Clarity": "clarity",
    "Weight": "weight",
    "Lab": "lab",
    "Digital Cert": "digital_cert",
    "Cut Grade": "cut_grade",
    "Polish": "polish",
    "Symmetry": "symmetry",
    "Fluor": "fluor",
    "Rapaport Price": "rapaport_price",
    "% Off RAP": "discount_off_rap",
    "Price/Ct": "price_per_carat",
    "Total Amount": "total_amount_inr",
    "Certificate #": "certificate_number",
    "Length": "length",
    "Width": "width",
    "Depth": "depth",
    "Depth %": "depth_percent",
    "Table %": "table_percent",
    "Girdle": "girdle",
    "Culet": "culet",
    "Description/Comments": "description",
    "Origin": "origin",
    "Memo Status": "memo_status",
    "Cert Link": "cert_link",
    "Diamond Image": "diamond_image_link",
    "Video": "video_link",
    "Shade": "shade"
}

# Insert data into the items table
def insert_into_items_table(json_data):
    conn = None
    try:
        # Establish database connection
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Prepare the data for insertion into the items table
        sku = json_data.get("Lot #")
        name = f"{json_data.get('Weight')} Carat {json_data.get('Shape')}"
        description = json_data.get("Description/Comments")
        category = "Diamonds"
        subcategory = "Lab Diamonds"
        material = None
        weight = json_data.get("Weight")
        vendor_id = 1
        storage_type = "bin"
        price = json_data.get("Total Amount")
        cost_price = json_data.get("Total Amount")

        # Insert into the items table
        insert_query = """
            INSERT INTO items (sku, name, description, category, subcategory, material, weight, vendor_id, storage_type, price, cost_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING item_id;
        """
        cur.execute(insert_query, (sku, name, description, category, subcategory, material, weight, vendor_id, storage_type, price, cost_price))
        
        # Get the generated item_id
        item_id = cur.fetchone()[0]
        conn.commit()
        return item_id
    
    except Exception as e:
        print(f"Error inserting into items table: {e}")
    
    finally:
        if conn:
            cur.close()
            conn.close()

# Insert data into the diamonds table
def insert_into_diamonds_table(mapped_data, item_id):
    conn = None
    try:
        # Establish database connection
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Add the item_id to the mapped data
        mapped_data['item_id'] = item_id

        # Create the insert query dynamically based on available data
        columns = mapped_data.keys()
        values = [mapped_data[column] for column in columns]

        insert_query = sql.SQL("""
            INSERT INTO diamonds ({})
            VALUES ({})
        """).format(
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() * len(values))
        )

        cur.execute(insert_query, values)
        conn.commit()
        print("Data inserted into diamonds successfully!")
    
    except Exception as e:
        print(f"Error inserting into diamonds table: {e}")
    
    finally:
        if conn:
            cur.close()
            conn.close()

# Map the JSON data to the diamonds table columns
def map_diamond_data(json_data):
    mapped_data = {}
    for json_key, db_column in json_to_db_mapping.items():
        if json_key in json_data:
            mapped_data[db_column] = json_data[json_key]
    
    # Set 'Type' column to 'Lab Diamonds'
    mapped_data['type'] = 'Lab Diamonds'
    
    return mapped_data

# Main function to process the JSON data and insert into both tables
def main():
    json_file = 'diamonds.json'  # Path to your JSON file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    for diamond_data in json_data:
        # First insert into the items table and get the item_id
        item_id = insert_into_items_table(diamond_data)

        # Map the diamond data for the diamonds table
        mapped_data = map_diamond_data(diamond_data)

        # Then insert into the diamonds table using the item_id
        insert_into_diamonds_table(mapped_data, item_id)

if __name__ == "__main__":
    main()
