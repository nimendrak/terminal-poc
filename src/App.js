import React, { Component, useState, useEffect } from "react";
import Terminal from "react-terminal-view";
import { io } from "socket.io-client";
import axios from "axios";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      lines: [],
    };
  }

  componentDidMount() {
    console.log("componentDidMount");

    socket = io('http://127.0.0.1:5000/');

    socket.on("status", (data) => {
      console.log("socket connected - " + socket.connected);
      console.log("socket id - " + socket.id);
      console.log(data);
    });
  }

  render() {
    return (
      <div>
        <Terminal lines={this.state.lines} />
      </div>
    );
  }
}
