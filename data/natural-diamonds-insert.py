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
    "Stock_NO": "lot_number",  # This maps to Lot #
    "Shape": "shape",
    "Color": "color",
    "Clarity": "clarity",
    "Carat": "weight",
    "Color_Shade": "shade",
    "Rap_Vlu": "rapaport_price",
    "Rap__": "discount_off_rap",
    "Pr_Ct": "price_per_carat",
    "Amount": "total_amount_inr",
    "CERT_NO": "certificate_number",
    "TD_": "depth_percent",
    "Tab_": "table_percent",
    "Cut": "cut_grade",
    "Polish": "polish",
    "Symmetry": "symmetry",
    "Fluorescent": "fluor",
    "Girdle": "girdle",
    "CUL": "culet",
    "Lab": "lab",
    "FancyColorDescription": "description",
    "ImageLink": "diamond_image_link",
    "CertificateLink": "cert_link",
    "VideoLink": "video_link"
}

# Helper function to parse and split measurement into length, width, and depth
def parse_measurement(measurement):
    try:
        # Split the measurement string and extract length, width, and depth
        l_w_d = measurement.split("x")
        length_width = l_w_d[0].split("-")
        length = float(length_width[0])
        width = float(length_width[1])
        depth = float(l_w_d[1])
        return length, width, depth
    except Exception as e:
        print(f"Error parsing measurement: {e}")
        return None, None, None

# Insert data into the items table
def insert_into_items_table(json_data):
    conn = None
    try:
        # Establish database connection
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Prepare the data for insertion into the items table
        sku = json_data.get("Stock_NO")
        name = f"{json_data.get('Carat')} Carat {json_data.get('Shape')}"
        description = json_data.get("FancyColorDescription", "")
        category = "Diamonds"
        subcategory = "Natural Diamonds"
        material = None
        weight = json_data.get("Carat")
        vendor_id = 2
        storage_type = "bin"
        price = json_data.get("Amount")
        cost_price = json_data.get("Amount")

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
def insert_into_diamonds_table(mapped_data, item_id, length, width, depth):
    conn = None
    try:
        # Establish database connection
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Add the item_id, length, width, and depth to the mapped data
        mapped_data['item_id'] = item_id
        mapped_data['length'] = length
        mapped_data['width'] = width
        mapped_data['depth'] = depth

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
    
    # Set 'Type' column to 'Natural Diamond'
    mapped_data['type'] = 'Natural Diamond'
    
    return mapped_data

# Main function to process the JSON data and insert into both tables
def main():
    json_file = 'natural_diamonds.json'  # Path to your JSON file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    for diamond_data in json_data:
        # First insert into the items table and get the item_id
        item_id = insert_into_items_table(diamond_data)

        # Map the diamond data for the diamonds table
        mapped_data = map_diamond_data(diamond_data)

        # Parse the measurement field into length, width, and depth
        length, width, depth = parse_measurement(diamond_data.get("Measurement"))

        # Then insert into the diamonds table using the item_id
        insert_into_diamonds_table(mapped_data, item_id, length, width, depth)

if __name__ == "__main__":
    main()
