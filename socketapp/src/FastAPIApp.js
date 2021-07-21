import React from "react";
// import io from "socket.io-client";
import Terminal from "react-terminal-view";
// import Terminal, { ColorMode, LineType } from 'react-terminal-ui';

class Dashboard extends React.Component {
  state = {
    logs: ["Backend Logs"],
    socketData: "",
  };

  componentWillUnmount() {
    const { ws } = this.state;
    ws.close();
    console.log("component unmounted");
  }

  componentDidMount() {
    console.log("component mounted");

    const ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = this.onMessage;
  }

  onMessage = (ev) => {
    const recv = JSON.parse(ev.data);
    console.log(recv.value);

    this.setState({
      logs: this.state.logs.concat(recv.value),
    });
  };

  render() {
    return (
      <div
        style={{
          height: "100%",
          width: "100%",
          display: "flex",
        }}
      >
        <Terminal lines={this.state.logs} />
      </div>
    );
  }
}
export default Dashboard;
