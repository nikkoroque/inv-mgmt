import { Item } from "./product";
import { SalesSummary } from "./sales";
import { PurchaseSummary } from "./purchases";
import { ExpenseByCategorySummary, ExpenseSummary } from "./expenses";

export interface DashboardMetrics {
  popularProducts: Item[];
  salesSummary: SalesSummary[];
  purchaseSummary: PurchaseSummary[];
  expenseSummary: ExpenseSummary[];
  expenseByCategorySummary: ExpenseByCategorySummary[];
}
