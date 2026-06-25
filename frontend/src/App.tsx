import React from "react";
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom";

import Home from "./pages/home";
import TestResults from "./pages/results";

const App = () => (
  <Router>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/tests/" component={TestResults} />
      <Redirect to="/" /> {/* catchall. can replace with 404 */}
    </Switch>
  </Router>
);

export default App;
