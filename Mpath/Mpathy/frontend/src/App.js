import React, { useState } from "react";
import Welcome from "react-welcome-page";
import { apiMethods } from "./components/twitterAPI/apis";
import "./App.css";

const welcomeConfig = {
  //image: require('./image_path/mypic1.png),
  text: "MPathy - we are here to help you with your kid",
  imageAnimation: "flipInX",
  textAnimation: "bounce",
  backgroundColor: "#FF3354",
  textcolor: "#002134"
};

class App extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = { user: "", data: {} };
  }

  getData = () => {
    apiMethods.getTestDataNoParams().then(data => {
      this.setState({ data });
    });
  };

  setUser = value => {
    this.setState({ user: value });
  };

  renderUserSearch = () => {
    return (
      <div className="App">
        <label>
          <section>Please type the name of you kid here</section>
          <input
            type="text"
            value={this.state.user}
            onChange={e => {
              this.setUser(e.target.value);
            }}
            placeholder="type name here..."
          />
        </label>
        <button className="btn btn-primary"> Search</button>

        <div>{this.state.user}</div>
        <div>
          <button className="btn btn-primary" onClick={this.getData}>
            {" "}
            get
          </button>
        </div>
        <div>{JSON.stringify(this.state.data)}</div>
      </div>
    );
  };
  render() {
    return (
      <React.Fragment>
        {this.renderUserSearch()}
        <Welcome loopduration={11000} data={[welcomeConfig]} />
      </React.Fragment>
    );
  }
}

export default App;
