import React, { Component, useState, useEffect } from "react";
import Terminal from "react-terminal-view";
import { io } from "socket.io-client";
import axios from 'axios'

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      lines: [],
    };
  }


  useEffect(() => {
    const socket = io.connect('http://127.0.0.1:5000/shell')
    socket.on('connect', (data) => console.log(data))

    socket.on('newdata', (data) => console.log(data))
  }, []);

  render() {
    return (
      <div>
        <Terminal lines={this.state.lines} />
      </div>
    );
  }
}
