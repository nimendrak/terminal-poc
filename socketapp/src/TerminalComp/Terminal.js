import React, { useState } from "react";
import Terminal, { ColorMode, LineType } from "react-terminal-ui";


class NewTerminal extends React.Component {
    state = {
        logs:["Backend Logs"],
        socketData: "",
    }

    // componentDidMount()

    TerminalController = (props = {}) => {
    const [terminalLineData] = useState([
        { type: LineType.Output, value: "Welcome to the React Terminal UI Demo!" },
    ]);
    // Terminal has 100% width by default so it should usually be wrapped in a container div
    return (
        <div>
        <Terminal
            name="React Terminal Usage Example"
            colorMode={ColorMode.Light}
            lineData={terminalLineData}
            onInput={(terminalInput) =>
            console.log(`New terminal input received: '${terminalInput}'`)
            }
        />
        </div>
    );
    }
}

export default NewTerminal;
