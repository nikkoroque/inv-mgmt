import { Request, Response } from "express";
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const getDashboardMetrics = async (
  req: Request,
  res: Response
): Promise<void> => {
  try {
    const expenseSummary = await prisma.expense_summary.findMany({
      take: 5,
      orderBy: {
        date: "desc",
      },
    });

    const expenseByCategorySummaryRaw =
      await prisma.expense_by_category.findMany({
        take: 5,
        orderBy: {
          date: "desc",
        },
      });

    const expenseByCategorySummary = expenseByCategorySummaryRaw.map(
      (item) => ({
        ...item,
        amount: item.amount.toString(),
      })
    );

    const popularProducts = await prisma.items.findMany({
      take: 50,
      orderBy: {
        item_id: "desc",
      },
    });

    const salesSummary = await prisma.sales_summary.findMany({
      take: 5,
      orderBy: {
        date: "desc",
      },
    });

    const purchaseSummary = await prisma.purchase_summary.findMany({
      take: 5,
      orderBy: {
        date: "desc",
      },
    });

    res.json({
      popularProducts,
      salesSummary,
      purchaseSummary,
      expenseSummary,
      expenseByCategorySummary,
    });
  } catch (error) {
    res
      .status(500)
      .json({ message: `${error} : Error retrieving dashbord metrics.` });
  }
};
