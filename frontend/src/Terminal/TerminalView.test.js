import React from 'react';
import ReactDOM from 'react-dom';
import TerminalView from 'Terminal.test.js';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<TerminalView />, div);
  ReactDOM.unmountComponentAtNode(div);
});
