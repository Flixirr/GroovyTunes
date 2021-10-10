import React, { Component } from 'react';
import { Link } from "react-router-dom";
import logo from "../img/logo-white.png";

const API_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/v1/users/auth/login/";

class Login extends Component {

    state = {
        credentials: {
            email: '',
            password: ''
        },
        errors: false
    }

    sendData = event => {
        event.preventDefault();

        fetch(API_AUTH_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.state.credentials)
        }).then(
            res => res.json()
        ).then(
            data => {
                if(data.key) {
                    localStorage.clear();
                    localStorage.setItem('token', data.key);
                    window.location.replace('http://127.0.0.1:3000/main');
                } else {
                    this.setState({
                        credentials:
                        {
                            email: '',
                            password: ''
                        }
                    });
                    localStorage.clear();
                    this.setState({errors: true});
                }
            }
        )
    }

    inputChanged = event => {
        const creds = this.state.credentials;

        creds[event.target.name] = event.target.value;

        this.setState({credentials: creds});
    }

    render() {
        return (
            <div className="centered-flex">
                <img style={{ width: '18vw', height: '15vw', margin: '0'}} src={logo} alt="Logo" />
                    <form onSubmit={this.sendData}>
                        <input className="input-field" type="email" placeholder="example@org.co" name="email"
                                value={this.state.credentials.email}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="password" placeholder="Password" name="password"
                                value={this.state.credentials.password}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-submit" type='submit' value='LOGIN' />
                    </form>
                {this.state.errors && <p style={{ color: "red" }}>Invalid credentials.</p>}
                <p className="text-normal">Don't have an account yet? <Link to="/register" className="text-link">Register!</Link></p>
                <p style={{ fontSize: '2vh' }} >Or go to <Link to="/main" className="text-link">main page</Link></p>
            </div>
        );
    }
}

export default Login;
