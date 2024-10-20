"use client";

import { useState } from "react"; // Import useState to manage dropdown open/close state
import { useAppDispatch, useAppSelector } from "@/app/redux"; // Redux hooks for accessing and dispatching state
import { setIsSidebarCollapsed } from "@/state"; // Action for toggling sidebar collapse state
import {
  Archive,
  Atom,
  Clipboard,
  Layout,
  LucideIcon,
  Menu,
  SlidersHorizontal,
  User,
  ChevronDown, // Icon for showing dropdown status
  ChevronRight,
  PencilRuler,
  CircleDollarSign,
  SquareKanban,
  CircleStop,
  Gem,
  LocateFixed,
  Combine, // Icon for showing dropdown status
} from "lucide-react"; // Icon imports
import Link from "next/link"; // Next.js link component for navigation
import { usePathname } from "next/navigation"; // Hook for getting the current path

interface SidebarLinkProps {
  href: string;
  icon: LucideIcon;
  label: string;
  isCollapsed: boolean;
}

// Component for individual sidebar links
const SidebarLink = ({
  href,
  icon: Icon,
  label,
  isCollapsed,
}: SidebarLinkProps) => {
  const pathname = usePathname(); // Get current route
  const isActive =
    pathname === href || (pathname === "/" && href === "/dashboard"); // Check if link is active

  return (
    <Link href={href}>
      <div
        className={`cursor-pointer flex items-center ${
          isCollapsed ? "justify-center py-4" : "justify-start px-8 py-4"
        } hover:text-blue-500 hover:bg-blue-100 gap-3 transition-colors ${
          isActive ? "bg-blue-200 text-white" : ""
        }`}
      >
        <Icon className="w-6 h-6 !text-gray-700" /> {/* Display icon */}
        <span
          className={`${
            isCollapsed ? "hidden" : "block"
          } font-medium text-gray-700`}
        >
          {label} {/* Display label */}
        </span>
      </div>
    </Link>
  );
};

// Component for dropdown categories
const SidebarDropdown = ({
  label,
  isCollapsed,
  children,
}: {
  label: string;
  isCollapsed: boolean;
  children: React.ReactNode;
}) => {
  const [isOpen, setIsOpen] = useState(false); // State to track whether the dropdown is open

  const toggleDropdown = () => {
    setIsOpen(!isOpen); // Toggle open/close state
  };

  return (
    <div>
      {/* Dropdown label with click handler to open/close */}
      <div
        className={`cursor-pointer flex items-center px-8 py-4 font-bold text-gray-500 justify-between ${
          isCollapsed ? "hidden" : "block"
        }`}
        onClick={toggleDropdown} // Toggle dropdown on click
      >
        {label}
        {/* Display Chevron based on whether dropdown is open */}
        {isOpen ? (
          <ChevronDown className="w-4 h-4 mr-2" />
        ) : (
          <ChevronRight className="w-4 h-4 mr-2" />
        )}
      </div>
      {/* Only show children (links) if dropdown is open */}
      {isOpen && <div>{children}</div>}
    </div>
  );
};

const Sidebar = () => {
  const currentYear = new Date().getFullYear(); // Get current year
  const dispatch = useAppDispatch(); // Get dispatch function for Redux
  const isSidebarCollapsed = useAppSelector(
    (state) => state.global.isSidebarCollapsed
  ); // Get sidebar collapse state from Redux

  // Function to toggle sidebar collapse state
  const toggleSidebar = () => {
    dispatch(setIsSidebarCollapsed(!isSidebarCollapsed));
  };

  // Determine sidebar width based on collapse state
  const sidebarClassNames = `fixed flex flex-col ${
    isSidebarCollapsed ? "w-0 md:w-16" : "w-72 md:w-64"
  } bg-white transition-all duration-300 overflow-hidden h-full shadow-md z-40`;

  return (
    <div className={sidebarClassNames}>
      {/* TOP LOGO */}
      <div
        className={`flex gap-3 justify-between md:justify-normal items-center pt-8 ${
          isSidebarCollapsed ? "px-5" : "px-8"
        }`}
      >
        {/* Display logo icon */}
        <div>
          <Atom className="w-8 h-8" />
        </div>
        {/* Display logo text */}
        <h1
          className={`font-extrabold text-2xl ${
            isSidebarCollapsed ? "hidden" : "block"
          }`}
        >
          NIROLiNK
        </h1>
        {/* Toggle button for collapsing sidebar */}
        <button
          className="md:hidden px-3 py-3 bg-gray-100 rounded-full hover:bg-blue-100"
          onClick={toggleSidebar}
        >
          <Menu className="w-4 h-4" />
        </button>
      </div>

      {/* LINKS */}
      <div className="flex-grow mt-8">
        {/* Dashboard link */}
        <SidebarLink
          href="/"
          icon={Layout}
          label="Dashboard"
          isCollapsed={isSidebarCollapsed}
        />

        {/* Inventory Management dropdown */}
        <SidebarDropdown
          label="Inventory Management"
          isCollapsed={isSidebarCollapsed}
        >
          <SidebarLink
            href="/inventory"
            icon={Archive}
            label="Inventory"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/items"
            icon={Clipboard}
            label="Item Master"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/jewelry"
            icon={CircleStop}
            label="Jewelry"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/diamonds"
            icon={Gem}
            label="Diamonds"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/profiling"
            icon={PencilRuler}
            label="Profiling"
            isCollapsed={isSidebarCollapsed}
          />
        </SidebarDropdown>
        {/* Inventory Management dropdown */}
        <SidebarDropdown
          label="Warehouse Management"
          isCollapsed={isSidebarCollapsed}
        >
          <SidebarLink
            href="/locations"
            icon={LocateFixed}
            label="Locations"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/storage-types"
            icon={Combine}
            label="Storage Types"
            isCollapsed={isSidebarCollapsed}
          />
        </SidebarDropdown>

        {/* Labor dropdown */}
        <SidebarDropdown
          label="Labor Management"
          isCollapsed={isSidebarCollapsed}
        >
          <SidebarLink
            href="/forecast"
            icon={SquareKanban}
            label="Forecast"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/expenses"
            icon={CircleDollarSign}
            label="Expenses"
            isCollapsed={isSidebarCollapsed}
          />
        </SidebarDropdown>

        {/* Administration dropdown */}
        <SidebarDropdown
          label="Administration"
          isCollapsed={isSidebarCollapsed}
        >
          <SidebarLink
            href="/users"
            icon={User}
            label="User Management"
            isCollapsed={isSidebarCollapsed}
          />
          <SidebarLink
            href="/settings"
            icon={SlidersHorizontal}
            label="Settings"
            isCollapsed={isSidebarCollapsed}
          />
        </SidebarDropdown>
      </div>

      {/* FOOTER */}
      <div>
        <p
          className={`${
            isSidebarCollapsed ? "hidden" : "block"
          } text-center text-xs text-gray-500`}
        >
          &copy; {currentYear} Nirolink WMS {/* Footer with copyright */}
        </p>
      </div>
    </div>
  );
};

export default Sidebar;
