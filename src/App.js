import React, { Component } from "react";
import Terminal from "react-terminal-view";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      lines: [],
      tempArr: [],
    };
  }

  async componentDidMount() {
    const url =
      "https://api.fungenerators.com/name/categories.json?start=0&limit=5";
    const response = await fetch(url);
    const data = await response.json();

    // this.setState({
    //   lines: [data.contents[0][0].name],
    // });

    for (var i = 0; i < 5; i++) {
      this.state.tempArr.push(data.contents[0][i].name);
    }

    this.setState({ lines: this.state.tempArr });

    console.log(this.state.lines);
  }

  render() {
    return (
      <div>
        <Terminal lines={this.state.lines} />
      </div>
    );
  }
}
