import React from "react";

import Header from "./header";

const Layout = ({ children, title }: {children: any, title: any}) => (
  <>
    <div className="pb-32">
      <Header />
      <header className="py-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-medium">{title}</h1>
        </div>
      </header>
    </div>
    <main className="-mt-32">
      <div className="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow px-5 py-6 sm:px-6" style={{minHeight: '300px'}}>
          {children}
        </div>
      </div>
    </main>
  </>
);

export default Layout;
