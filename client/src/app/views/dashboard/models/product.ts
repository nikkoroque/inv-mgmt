export interface Item {
  item_id: number; // Primary key, unique identifier for each item
  sku: string; // Stock keeping unit, unique for each item
  name: string; // Name of the item
  description?: string; // Optional detailed description of the item
  category: string; // Primary category (e.g., "Jewelry", "Diamond")
  subcategory?: string; // Optional subcategory of the item
  material?: string; // Optional material of the item (e.g., "Gold", "Platinum")
  weight?: number; // Optional weight of the item in grams or carats
  vendor_id?: number; // Foreign key referencing the vendor ID (optional)
  storage_type?: string; // Optional type of storage used for the item
  stock_quantity: number; // Quantity of the item available in stock
  low_stock_qty: number; // Safety stock value of the item
  price: number; // Selling price of the item
  cost_price: number; // Cost price of the item
  created_at: string; // Timestamp of when the item record was created (ISO string)
  updated_at: string; // Timestamp of the last update made to the item record (ISO string)
  item_image: string;
}
