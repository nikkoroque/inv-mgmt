// "use client" directive is required when using client-side rendering for Next.js
"use client";

import React from "react";
import Navbar from "@/app/shared/(components)/Navbar"; // Importing the Navbar component
import Sidebar from "@/app/shared/(components)/Sidebar"; // Importing the Sidebar component
import StoreProvider from "@/app/redux"; // Importing the Redux store provider to wrap the app with Redux state

// DashboardLayout component defines the layout structure for the dashboard
// It includes a sidebar, a navbar, and a main content area where the `children` will be rendered
const DashboardLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className={`light flex bg-gray-50 text-gray-900 w-full min-h-screen`}>
      {/* Sidebar component is displayed on the left */}
      <Sidebar />
      {/* Main content area with Navbar and children */}
      <main
        className={`flex flex-col w-full h-full py-7 px-9 bg-gray-50 md:pl-24`}
      >
        {/* Navbar component */}
        <Navbar />
        {/* Render the passed children, which represents the page-specific content */}
        {children}
      </main>
    </div>
  );
};

// DashboardWrapper wraps the layout in the Redux store provider
// This ensures that Redux state is available to all components in the dashboard
const DashboardWrapper = ({ children }: { children: React.ReactNode }) => {
  return (
    // Wrap the layout in the StoreProvider to give access to Redux store
    <StoreProvider>
      {/* DashboardLayout is used to define the structure, and the children are passed down */}
      <DashboardLayout>{children}</DashboardLayout>
    </StoreProvider>
  );
};

// Export the wrapper component as default so it can be used in other parts of the app
export default DashboardWrapper;
