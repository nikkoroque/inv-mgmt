export interface ExpenseSummary {
  expense_summaryId: string;
  total_expenses: number;
  date: Date;
  expense_by_category: ExpenseByCategorySummary[];
}

export interface ExpenseByCategorySummary {
  expense_by_categoryId: string;
  expense_summaryId: string;
  date: Date;
  category: string;
  amount: string;
}
