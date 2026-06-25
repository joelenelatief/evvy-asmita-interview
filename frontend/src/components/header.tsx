import React from "react";
import { Link } from "react-router-dom";
import { withRouter } from "react-router";

const Header = () => {
  return (
    <nav className="">
      <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
        <div className="border-b">
          <div className="flex items-center justify-between h-16 px-4 sm:px-0">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <Link to="/">
                  <img
                    className="h-6"
                    src="https://endlessfrontierlabs.com/wp-content/uploads/2024/09/Evvy-Logo-Black.png"
                    alt="Evvy logo"
                  />
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default withRouter(Header);
