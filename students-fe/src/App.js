import logo from './logo.svg';
import './App.css';
import React, { Component, Fragment } from "react";
import Home from "./components/Home";
import Header from './components/Header';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Home />
      </Fragment>
    );
  }
}

export default App;