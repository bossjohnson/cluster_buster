import React, { Component } from 'react';
import './App.css';

class App extends Component {
  componentWillMount() {
    console.log('about to mount...');
  }

  componentDidMount() {
    console.log('mounted!');
  }

  render() {
    return (
      <div>
        Hello world!
      </div>
    );
  }
}

export default App;
