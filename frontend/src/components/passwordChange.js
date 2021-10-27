import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "semantic-ui-react";
import Cookies from 'js-cookie';

import logo from "../img/blank-profile-picture-973460_1280.png";

export function PasswordChange(props) {

    const [old_password, setOldPwd] = useState('');
    const [new_password, setNewPwd] = useState('');
    const [confirm_new_password, confirmNewPwd] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const sendData = event => {
        event.preventDefault();

        let formData = new FormData();

        formData.append('old_password', old_password);
        formData.append('new_password', new_password);
        formData.append('confirm_new_password', confirm_new_password);

        fetch('http://127.0.0.1:8000/api/users/rest/change_password', {
            method: 'PATCH',
            headers: {
                Authorization: `Token ${Cookies.get('token')}`
            },
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if(data.response) {
                    setSuccess(data.response);
                    setError('');
                } else if (data.old_password) {
                    setError(data.old_password);
                    setSuccess('');
                } else {
                    setError('Passwords don\'t match');
                    setSuccess('');
                }
            });
    };

    return (
        <div className="profile-layout">
            <img className="profile-pic" src={logo} alt="Profile picture" />
            <br />
            <div className="profile-info">
                <form onSubmit={sendData}>
                    <p>OLD PASSWORD</p>
                        <input type="password" className="info-box" 
                        onChange={e => setOldPwd(e.target.value)} />
                    <br />
                    <p>NEW PASSWORD</p>
                        <input type="password" className="info-box" 
                        onChange={e => setNewPwd(e.target.value)} />
                    <br />
                    <p>CONFIRM NEW PASSWORD</p>
                        <input type="password" className="info-box" 
                        onChange={e => confirmNewPwd(e.target.value)} />
                    <br />
                    <br />

                    <input className="input-submit" type='submit' value='SUBMIT' />

                    {error && <p style={{ color: "red" }}>{error}</p>}
                    {success && <p style={{ color: "green" }}>{success}</p>}
                </form>
            </div>
        </div>
    );
}
