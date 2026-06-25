import React from "react";
import { Link } from "react-router-dom";

import Layout from "../components/layout";

const Home = () => {
  return (
    <Layout title="Home">
      <div>
        View the{" "}
        <Link to="/tests/" className="underline">test results</Link>.
      </div>
    </Layout>
  );
};

export default Home;
