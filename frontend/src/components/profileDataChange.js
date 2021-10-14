import React from "react";
import { Link } from "react-router-dom";
import { Button } from "semantic-ui-react";

import logo from "../img/blank-profile-picture-973460_1280.png";

export function ProfileChangeData(props) {

    const profileData = props.profile;

    const sendData = event => {
        event.preventDefault();

        fetch(`http://127.0.0.1:8000/search/${this.state.searchQuery.replaceAll(' ', '-')}`)
            .then(response => response.json())
            .then(data => {
                /* 
                First array:
                    -> Artist name
                    -> Artist genius link
                Second array:
                    -> Song title
                    -> Genius link
                    -> Release date
                    -> Featured artists
                    -> Producers
                */
                console.log(data)
                this.setState({ searchResults: data });
                console.log(this.state.searchResults);
            });
    };
        
    return (
        <div className="profile-layout">
            <img className="profile-pic" src={logo} alt="Profile picture" />
            <br />
            <div className="profile-info">
                <form>
                    <p>USERNAME</p>
                        <input type="text" placeholder={profileData.username} className="info-box" />
                    <br />
                    <p>FIRST NAME (optional)</p>
                        <input type="text" placeholder={profileData.first_name} className="info-box" />
                    <br />
                    <p>LAST NAME (optional)</p>
                        <input type="text" placeholder={profileData.last_name} className="info-box" />
                    <br />
                    <br />

                    <input className="input-submit" type='submit' value='SUBMIT' />
                </form>
            </div>
        </div>
    );
}
