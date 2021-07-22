import React, { useEffect, useState } from "react";
import Terminal, { ColorMode, LineType } from "react-terminal-ui";
import './TerminalView.css';

const ws = new WebSocket("ws://localhost:8000/shell");

const TerminalController = ({ props }) => {
  const [terminalLineData, setTerminalLineData] = useState([]);

  useEffect(() => {
    ws.onopen = () => {
      // on connecting, do nothing but log it to the console
      console.log("connected");
    };

    ws.onmessage = (evt) => {
      // listen to data sent from the websocket server
      const response = JSON.parse(evt.data);
      setTerminalLineData((currentData) => [...currentData, response]);
      console.log(response);
    };

    ws.onclose = () => {
      console.log("disconnected");
      // automatically try to reconnect on connection loss
    };
  }, []);

  // Terminal has 100% width by default so it should usually be wrapped in a container div
  return (
    <div className="container">
      <Terminal
        name="Backend Logs"
        colorMode={ColorMode.Dark}
        lineData={terminalLineData}
        onInput={(terminalInput) =>
          console.log(`New terminal input received: '${terminalInput}'`)
        }
      />
    </div>
  );
};

export default TerminalController;
