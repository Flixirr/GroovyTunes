import React from "react";
import { Link } from "react-router-dom";

export function Profile(props) {

    const profileData = props.profile;

    if(props.isLoggedIn) {
        return (
            <div style={{display: 'flex', flexDirection: 'column'}}>
                <h1>Welcome back!</h1>
                <br />
                <p>Username: {profileData.username}</p>
                <br />
                <p>E-mail: {profileData.email}</p>
                <br />
                <p>First name (optional): {profileData.first_name}</p>
                <br />
                <p>Last name (optional): {profileData.last_name}</p>
            </div>
        );
    } else {
        return (
            <span>Seems you don't have a profile yet. Do you want to <Link to="/register">create one?</Link></span>
        );
    }

}
