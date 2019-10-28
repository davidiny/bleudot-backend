import React from "react";
import DataProvider from "./DataProvider";
import Discover from './Discover';
import Nav from './Nav';
import '../stylesheets/App.css';

const App = () => (
  <React.Fragment>
    <Nav />
    <DataProvider endpoint="api/events" 
                  render={data => <Discover data={data} />} />
  </React.Fragment>
);

export default App;
