import React from "react";
import io from "socket.io-client";
import Terminal from "react-terminal-view";
// import Terminal, { ColorMode, LineType } from 'react-terminal-ui';

class TerminalView extends React.Component {
  state = {
    logs: ["Backend Logs"],
    socketData: "",
  };

  componentWillUnmount() {
    const {ws, interval} = this.state;
    ws.close()
    clearInterval(interval)
  }

  componentDidMount() {
   const ws = new WebSocket('ws://localhost:8000/shell')
    ws.onmessage = this.onMessage

    console.log("component mounted");
  }

  onMessage = (ev) => {
    const recv = JSON.parse(ev.data)
    console.log(recv.value)
    this.socketData = recv.value
    this.setState({
      logs: this.state.logs.concat(this.socketData),
    });
  }

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
export default TerminalView;
