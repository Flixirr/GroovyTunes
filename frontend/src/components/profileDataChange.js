import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "semantic-ui-react";
import Cookies from 'js-cookie';

import logo from "../img/blank-profile-picture-973460_1280.png";

export function ProfileChangeData(props) {

    const profileData = props.profile;

    const email = profileData.email;

    const [username, setUsername] = useState('');
    const [first_name, setFirstName] = useState(profileData.first_name);
    const [last_name, setLastName] = useState(profileData.last_name);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const sendData = event => {
        event.preventDefault();

        let formData = new FormData();

        formData.append('email', email);
        formData.append('username', username);
        formData.append('first_name', first_name);
        formData.append('last_name', last_name);

        fetch('http://127.0.0.1:8000/api/users/rest/properties/update', {
            method: 'PUT',
            headers: {
                Authorization: `Token ${Cookies.get('token')}`
            },
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if(data.username || data.first_name || data.last_name) {
                    setError('Username is required');
                    setSuccess('');
                } else {
                    setSuccess('Data changed successfully, logout and login to refresh.');
                    setError('');
                }
            });
    };

    return (
        <div className="profile-layout">
            <img className="profile-pic" src={logo} alt="Profile picture" />
            <br />
            <div className="profile-info">
                <form onSubmit={sendData}>
                    <p>USERNAME</p>
                        <input type="text" placeholder={profileData.username} className="input-field"
                        style={{ fontSize: '1em'}} 
                        onChange={e => setUsername(e.target.value)} />
                    <br />
                    <p>FIRST NAME</p>
                        <input type="text" placeholder={profileData.first_name} className="input-field"
                        style={{ fontSize: '1em'}} 
                        onChange={e => setFirstName(e.target.value)} />
                    <br />
                    <p>LAST NAME</p>
                        <input type="text" placeholder={profileData.last_name} className="input-field"
                        style={{ fontSize: '1em'}} 
                        onChange={e => setLastName(e.target.value)} />
                    <br />
                    <br />

                    <input className="ui green inverted button btn-centered" type='submit' value='SUBMIT' />

                    {error && <p style={{ color: "red" }}>{error}</p>}
                    {success && <p style={{ color: "green" }}>{success}</p>}
                </form>
            </div>
        </div>
    );
}
