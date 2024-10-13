// Import required functions from Redux Toolkit Query
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query";

// Define the API service using Redux Toolkit's `createApi`
// This setup allows for efficient data fetching, caching, and synchronization with the Redux store
export const api = createApi({
  // The baseQuery function is responsible for making API requests.
  // `fetchBaseQuery` is a lightweight wrapper around fetch that can be used as the base for your requests.
  // The base URL for all API calls is defined by an environment variable `NEXT_PUBLIC_API_BASE_URL`
  baseQuery: fetchBaseQuery({ baseUrl: process.env.NEXT_PUBLIC_API_BASE_URL }),

  // A unique key to store this API reducer in the Redux state
  reducerPath: "api",

  // `tagTypes` allows you to define the types of cache tags, which can be used to invalidate or refetch data.
  // This can be useful when managing the cache and keeping the UI up-to-date.
  tagTypes: [],

  // Define the API endpoints. Each key in the object is a different endpoint that you can query.
  // Endpoints are functions that describe how to fetch data and can be added here.
  endpoints: (build) => ({}),
});

// Export the API service so it can be used throughout the application
// You can add your API endpoint definitions inside `endpoints` and export them from here.
export const {} = api;
