import React, { Component } from 'react';
import Autosuggest from 'react-autosuggest';

import './App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      username: ''
    }
  }

  handleUsername(evt){
    evt.preventDefault();
    // API Call to RIOT
  }

  render() {
    return (
      <div className="App">
        <div className="nav-bar-background">
          <div className="nav-bar">
            <ul>
              <li className="nav-bar nav"><a href="#">HOME</a></li>
              <li className="nav-bar nav"><a href="https://en.wikipedia.org/wiki/List_of_Unicode_characters">SPECIAL CHARACTERS</a></li>
            </ul>
          </div>
        </div>
        <div className="main-search">
          <div className="title"> IDLE<font color="blue">BUILDER</font> </div>
          <div className="subtitle">  IDLEBUILDER is the number one place to check if the Fortnite name YOU want is available. <br />
          </div>
          <form className="search-username-form" onSubmit={evt => this.handleUsername(evt, this.state.username)} >
            <input type="text" className="search-username-form input" placeholder="Search Display Name..." value={this.state.username} onChange={evt => this.setState({ username: evt.target.value })} required />
            <button type="submit" className="search-username-form btn">GO</button>
          </form>
        </div>
      </div>
    );
  }
}

export default App;
