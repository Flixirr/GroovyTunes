import React from "react";
import { Link } from "react-router-dom";
import { Button } from "semantic-ui-react";

import logo from "../img/blank-profile-picture-973460_1280.png";

export function Profile(props) {

    const profileData = props.profile;

    if(props.isLoggedIn) {
        return (
            <div className="profile-layout">
                <img className="profile-pic" src={logo} alt="Profile picture" />
                <br />
                <div className="profile-info">
                    <p>USERNAME</p>
                        <input type="text" value={profileData.username} className="info-box" readOnly />
                    <br />
                    <p>E-MAIL </p>
                        <input type="text" value={profileData.email} className="info-box" readOnly />
                    <br />
                    <p>FIRST NAME (optional)</p>
                        <input type="text" value={profileData.first_name} className="info-box" readOnly />
                    <br />
                    <p>LAST NAME (optional)</p>
                        <input type="text" value={profileData.last_name} className="info-box" readOnly />
                    <br />
                    <br />
                </div>

                <Link to="/users/data/change">
                    <Button className="profile-button">
                            CHANGE DATA
                    </Button>
                </Link>
            </div>
        );
    } else {
        return (
            <div className="profile-layout">
                <p style={{color: 'white', fontSize: '4vh'}}>Seems you don't have a profile yet. Do you want to <Link to="/register" className="text-link">create one?</Link></p>
            </div>
            
        );
    }

}
