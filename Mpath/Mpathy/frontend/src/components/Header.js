import React from "react";
import logo from "../../src/Mpathy.png";

function Header(props) {
  return (
    <div className="headerWrapper">
      <div className="headerLogo animated fadeInLeft">
        <img
          src={logo}
          alt={"logo"}
          style={{ width: "70px", height: "70px" }}
        />
      </div>
      <div className="headerSlogan animated fadeInRight">
        <span>We are here to help you</span>
      </div>
    </div>
  );
}

export default Header;
