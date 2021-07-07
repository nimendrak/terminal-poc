import React, { Component } from "react";
import Terminal from "react-terminal-view";

export default class App extends Component {
  render() {
    let lines = [
      "Hello,",
      "My name's Amine",
      "I'm a full-stack developer",
      "I love everything that's related to new technology",
      "I hope this component has been useful to you"
    ];
    return (
      <div>
        <Terminal lines={lines} />
      </div>
    );
  }
}
