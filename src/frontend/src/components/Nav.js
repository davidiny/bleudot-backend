import React, {Component} from 'react';
import Setting from "../images/setting.svg";
import Profile from "../images/profile.svg";


class Nav extends Component {
	render() {
		return (
			<div className="navbar">
				<div className="navbar-container container">
					<div className="navbar-menu">
						<a className="active" href=".">Discover</a>
						<a href=".">Create </a>
					</div>
					<div className="navbar-title">
						<a href=".">BleuDot </a>
					</div>
					<div className="navbar-buttons">
						<div className="navbar-button-icon"><img src={Setting} /></div>
						<div className="navbar-button-icon"><img src={Profile} /></div>
					</div>
				</div>
			</div>
		);
	}
}

export default Nav;