-- Item Master Table
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50),
    material VARCHAR(50),
    weight NUMERIC(10, 2),
    vendor_id INT REFERENCES vendors(vendor_id),
    storage_type VARCHAR(50),
    stock_quantity INT DEFAULT 0,
    low_stock_qty INT DEFAULT 0,
    price NUMERIC(10, 2),
    cost_price NUMERIC(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE items IS 'Table containing basic information about items, including jewelry and diamonds.';
COMMENT ON COLUMN items.item_id IS 'Primary key, unique identifier for each item.';
COMMENT ON COLUMN items.sku IS 'Stock keeping unit, unique for each item.';
COMMENT ON COLUMN items.name IS 'Name of the item.';
COMMENT ON COLUMN items.description IS 'Detailed description of the item.';
COMMENT ON COLUMN items.category IS 'Primary category (e.g., "Jewelry", "Diamond").';
COMMENT ON COLUMN items.subcategory IS 'Subcategory of the item (e.g., "Ring", "Necklace").';
COMMENT ON COLUMN items.material IS 'Material of the item (e.g., "Gold", "Platinum").';
COMMENT ON COLUMN items.weight IS 'Weight of the item in grams or carats.';
COMMENT ON COLUMN items.vendor_id IS 'Foreign key to the vendors table.';
COMMENT ON COLUMN items.storage_type IS 'Type of storage used for the item (e.g., "Safe", "Display Case").';
COMMENT ON COLUMN items.low_stock_qty IS 'Safety stock value of the item.';
COMMENT ON COLUMN items.stock_quantity IS 'Quantity of the item available in stock.';
COMMENT ON COLUMN items.price IS 'Selling price of the item.';
COMMENT ON COLUMN items.cost_price IS 'Cost price of the item.';
COMMENT ON COLUMN items.created_at IS 'Timestamp of when the item record was created.';
COMMENT ON COLUMN items.updated_at IS 'Timestamp of the last update made to the item record.';

-- Diamonds Table
CREATE TABLE diamonds (
    diamond_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES items(item_id),
    carat_weight NUMERIC(10, 2),
    clarity VARCHAR(50),
    color VARCHAR(50),
    cut VARCHAR(50),
    fluorescence VARCHAR(50),
    origin VARCHAR(255),
    certification VARCHAR(255)
);

COMMENT ON TABLE diamonds IS 'Table storing detailed information about diamonds.';
COMMENT ON COLUMN diamonds.diamond_id IS 'Primary key, unique identifier for each diamond.';
COMMENT ON COLUMN diamonds.item_id IS 'Foreign key to the items table.';
COMMENT ON COLUMN diamonds.carat_weight IS 'Carat weight of the diamond.';
COMMENT ON COLUMN diamonds.clarity IS 'Clarity grade of the diamond (e.g., "VVS1", "SI1").';
COMMENT ON COLUMN diamonds.color IS 'Color grade of the diamond (e.g., "D", "G").';
COMMENT ON COLUMN diamonds.cut IS 'Cut type of the diamond (e.g., "Round Brilliant", "Emerald").';
COMMENT ON COLUMN diamonds.fluorescence IS 'Fluorescence level of the diamond (e.g., "None", "Faint").';
COMMENT ON COLUMN diamonds.origin IS 'Origin of the diamond.';
COMMENT ON COLUMN diamonds.certification IS 'Certification details of the diamond (e.g., GIA certification).';

-- Jewelry Table
CREATE TABLE jewelry (
    jewelry_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES items(item_id),
    metal_type VARCHAR(50),
    gemstone_type VARCHAR(100),
    total_weight NUMERIC(10, 2),
    num_diamonds INT,
    diamond_weight NUMERIC(10, 2),
    setting_type VARCHAR(100)
);

COMMENT ON TABLE jewelry IS 'Table storing detailed information about finished jewelry.';
COMMENT ON COLUMN jewelry.jewelry_id IS 'Primary key, unique identifier for each jewelry piece.';
COMMENT ON COLUMN jewelry.item_id IS 'Foreign key to the items table.';
COMMENT ON COLUMN jewelry.metal_type IS 'Type of metal used for the jewelry piece (e.g., "Gold", "Silver").';
COMMENT ON COLUMN jewelry.gemstone_type IS 'Type of gemstone used in the jewelry (e.g., "Ruby", "Emerald").';
COMMENT ON COLUMN jewelry.total_weight IS 'Total weight of the jewelry piece in grams.';
COMMENT ON COLUMN jewelry.num_diamonds IS 'Number of diamonds embedded in the jewelry piece.';
COMMENT ON COLUMN jewelry.diamond_weight IS 'Total carat weight of the diamonds in the jewelry piece.';
COMMENT ON COLUMN jewelry.setting_type IS 'Type of setting used in the jewelry (e.g., "Prong", "Bezel").';

-- Vendor Table
CREATE TABLE vendors (
    vendor_id SERIAL PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT
);

COMMENT ON TABLE vendors IS 'Table storing vendor details for items.';
COMMENT ON COLUMN vendors.vendor_id IS 'Primary key, unique identifier for each vendor.';
COMMENT ON COLUMN vendors.vendor_name IS 'Vendor name (e.g., "ABC Jewelers").';
COMMENT ON COLUMN vendors.contact_person IS 'Contact person at the vendor.';
COMMENT ON COLUMN vendors.contact_number IS 'Contact number for the vendor.';
COMMENT ON COLUMN vendors.email IS 'Email address of the vendor.';
COMMENT ON COLUMN vendors.address IS 'Vendor’s physical address.';

-- Sales Table
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES items(item_id),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity INT,
    sale_price NUMERIC(10, 2),
    customer_id INT REFERENCES customers(customer_id)
);

COMMENT ON TABLE sales IS 'Table recording sales transactions.';
COMMENT ON COLUMN sales.sale_id IS 'Primary key, unique identifier for each sale.';
COMMENT ON COLUMN sales.item_id IS 'Foreign key to the items table.';
COMMENT ON COLUMN sales.sale_date IS 'Date and time of the sale.';
COMMENT ON COLUMN sales.quantity IS 'Quantity of items sold in the transaction.';
COMMENT ON COLUMN sales.sale_price IS 'Total selling price for the transaction.';
COMMENT ON COLUMN sales.customer_id IS 'Foreign key to the customers table.';

-- Inventory Table
CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES items(item_id),
    stock_quantity INT DEFAULT 0,
    zone VARCHAR(3),
    aisle VARCHAR(2),
    bay VARCHAR(3),
    level VARCHAR(2),
    position VARCHAR(1),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE inventory IS 'Table tracking inventory details for items.';
COMMENT ON COLUMN inventory.inventory_id IS 'Primary key, unique identifier for each inventory record.';
COMMENT ON COLUMN inventory.item_id IS 'Foreign key to the items table.';
COMMENT ON COLUMN inventory.stock_quantity IS 'Quantity of items available in stock.';
COMMENT ON COLUMN inventory.zone IS 'Zone within the warehouse (e.g., "A00").';
COMMENT ON COLUMN inventory.aisle IS 'Aisle within the zone (e.g., "01").';
COMMENT ON COLUMN inventory.bay IS 'Bay within the aisle (e.g., "001").';
COMMENT ON COLUMN inventory.level IS 'Level within the bay (e.g., "01").';
COMMENT ON COLUMN inventory.position IS 'Position within the level (e.g., "A").';
COMMENT ON COLUMN inventory.last_updated IS 'Timestamp of the last update made to the inventory record.';

-- Customer Table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT
);

COMMENT ON TABLE customers IS 'Table storing customer details.';
COMMENT ON COLUMN customers.customer_id IS 'Primary key, unique identifier for each customer.';
COMMENT ON COLUMN customers.customer_name IS 'Customer’s full name.';
COMMENT ON COLUMN customers.contact_number IS 'Contact number for the customer.';
COMMENT ON COLUMN customers.email IS 'Email address of the customer.';
COMMENT ON COLUMN customers.address IS 'Customer’s physical address.';

-- Storage Types Table
CREATE TABLE storage_types (
    storage_type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL
);

COMMENT ON TABLE storage_types IS 'Table defining different storage types for items (e.g., Safe, Display Case).';
COMMENT ON COLUMN storage_types.storage_type_id IS 'Primary key, unique identifier for each storage type.';
COMMENT ON COLUMN storage_types.type_name IS 'Name of the storage type (e.g., "Safe", "Display Case").';

-- Sample indexes
CREATE INDEX idx_items_sku ON items(sku);
CREATE INDEX idx_inventory_location ON inventory(zone, aisle, bay, level, position);
