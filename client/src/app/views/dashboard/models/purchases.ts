export interface Purchase {
  purchaseId: string;
  productId: string;
  timestamp: Date;
  quantity: number;
  unitCost: number;
  landedCost: number;
  totalCost: number;
}

export interface PurchaseSummary {
  purchase_summaryId: string;
  total_purchased: number;
  change_percentage?: number;
  date: Date;
}
