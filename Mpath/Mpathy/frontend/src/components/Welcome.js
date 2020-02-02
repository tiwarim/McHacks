import React from "react";
import logo from "../../src/Mpathy.png";

class WelcomePage extends React.PureComponent {
  renderBtn = () => {
    return (
      <div style={{ marginTop: "100px", marginLeft: "100px" }}>
        <span className="btn animated fadeIn" onClick={this.props.clicked}>
          Begin
        </span>
      </div>
    );
  };

  render() {
    return (
      <div className="welcomeWrapper">
        <div className="logo ">
          <div className="animated fadeInDown">
            <img src={logo} alt="logo" />
          </div>
          <div className="slogan animated fadeIn">We are here to help you!</div>
          {this.renderBtn()}
        </div>
      </div>
    );
  }
}

export default WelcomePage;
