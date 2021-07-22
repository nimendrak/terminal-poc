import React, {useState} from "react";
// import Terminal from "react-terminal-view";
import Terminal, { ColorMode, LineType } from "react-terminal-ui";

class TerminalView extends React.Component {
  state = {
    logs: ["Backend Logs"],
    socketData: "",
  };

  componentWillUnmount() {
    const { ws, interval } = this.state;
    ws.close();
    clearInterval(interval);
  }

  componentDidMount() {
    const ws = new WebSocket("ws://localhost:8000/shell");
    ws.onmessage = this.onMessage;

    this.setState({
      ws: ws,
      // Create an interval to send echo messages to the server
      interval: setInterval(() => ws.send("echo"), 1000),
    });

    console.log("component mounted");
  }

  onMessage = (ev) => {
    const recv = JSON.parse(ev.data);
    console.log(recv.value);
    this.socketData = recv.value;
    this.setState({
      logs: this.state.logs.concat(this.socketData),
    });
  };

  render() {
    return (
      <div className="container">
        {/* <Terminal
          name="CloudTerra Backend Logs"
          colorMode={ColorMode.Dark}
          lineData={this.logs}
          onInput={(terminalInput) =>
            console.log(`New terminal input received: '${terminalInput}'`)
          }
        /> */}
      </div>
    );
  }
}
export default TerminalView;
