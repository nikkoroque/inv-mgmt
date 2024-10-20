export interface Sales {
  saleId: string;
  productId: string;
  timestamp: Date;
  quantity: number;
  unit_price: number;
  total_amount: number;
}

export interface SalesSummary {
  sales_summaryId: string;
  total_value: number;
  change_percentage?: number;
  date: Date;
}
