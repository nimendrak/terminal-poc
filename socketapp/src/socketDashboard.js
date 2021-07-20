import React from "react";
import io from "socket.io-client";
import Terminal from "react-terminal-view";
// import Terminal, { ColorMode, LineType } from 'react-terminal-ui';

class Dashboard extends React.Component {
  state = {
    logs: ["Backend Logs"],
    socketData: "",
  };

  componentWillUnmount() {
    this.socket.close();
    console.log("component unmounted");
  }

  componentDidMount() {
    var sensorEndpoint = "http://localhost:5000";
    this.socket = io.connect(sensorEndpoint, {
      reconnection: true,
      // transports: ['websocket']
    });
    console.log("component mounted");
    this.socket.on("responseMessage", (message) => {
      this.setState({ socketData: message.log });
      console.log("responseMessage", message);
      this.setState({
        logs: this.state.logs.concat(this.state.socketData),
      });
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
export default Dashboard;
