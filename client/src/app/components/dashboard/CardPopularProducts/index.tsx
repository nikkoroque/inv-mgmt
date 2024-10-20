import Rating from "@/app/shared/(components)/Rating";
import { useGetDashboardMetricsQuery } from "@/app/views/dashboard/api/api";
import { ShoppingBag } from "lucide-react";
import Image from "next/image";
import React from "react";

const CardPopularProducts = () => {
  const { data: dashboardMetrics, isLoading } = useGetDashboardMetricsQuery();

  // function getRandomSalesQty() {
  //   const randomMultiplier = Math.floor(Math.random() * 100) + 1;
  //   const randomQty = randomMultiplier * 1000;

  //   return randomQty;
  // }
  return (
    <div className="row-span-3 xl:row-span-6 bg-white shadow-md rounded-2xl pb-16">
      {isLoading ? (
        <div className="m-5">Loading...</div>
      ) : (
        <>
          <h3 className="text-lg font-semibold px-7 pt-5 pb-2">
            Popular Products
          </h3>
          <hr />
          <div className="overflow-auto h-full">
            {dashboardMetrics?.popularProducts.map((product) => (
              <div
                key={product.item_id}
                className="flex items-center justify-between gap-3 px-5 py-7 border-b"
              >
                <div className="flex items-center gap-3">
                  <div>
                    <Image
                      src={product.item_image}
                      alt="image"
                      width={40}
                      height={40}
                    />
                  </div>
                  <div className="flex flex-col justify-between gap-1">
                    <div className="font-bold text-gray-700">
                      {product.name}
                    </div>
                    <div className="flex text-sm items-center">
                      <span className="font-bold text-blue-500 text-xs">
                        {product.price}
                      </span>
                      <span className="mx-2">|</span>
                      <div>{product.subcategory}</div>
                      <Rating rating={product?.price || 0} />
                    </div>
                  </div>
                </div>
                <div className="text-xs flex items-center">
                  <button className="p-2 rounded-full bg-blue-100 text-blue-600 mr-2">
                    <ShoppingBag className="w-4 h-4" />
                  </button>
                  {Math.round(Math.floor(Math.random() * 100) + 1)}k sold
                </div>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default CardPopularProducts;
