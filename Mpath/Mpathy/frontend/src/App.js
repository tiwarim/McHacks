import React, { useState } from "react";
import { apiMethods } from "./components/twitterAPI/apis";
import WelcomePage from "./components/Welcome";
import { Button, Form, FormGroup, Label, Input } from "reactstrap";
import Header from "./components/Header";

import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = { user: "", data: {}, begin: false };
  }

  setUser = value => {
    this.setState({ user: value });
  };

  begin = () => {
    this.setState({ begin: true });
  };

  renderUserSearch = () => {
    return (
      <div className="App">
        <Header />
        <Form className="form">
          <FormGroup>
            <Label for="exampleEmail">
              Please start by typing you kids name
            </Label>
            <Input
              type="text"
              value={this.state.user}
              onChange={e => {
                this.setUser(e.target.value);
              }}
              placeholder="type name here..."
            />
          </FormGroup>
        </Form>
        <Button className="btn btn-primary"> Search</Button>
        <div>{this.state.user}</div>
      </div>
    );
  };
  render() {
    return (
      <div className="welcomeWrapper">
        {this.state.begin ? (
          this.renderUserSearch()
        ) : (
          <WelcomePage clicked={this.begin} />
        )}
      </div>
    );
  }
}

export default App;
