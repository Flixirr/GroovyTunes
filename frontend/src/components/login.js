import React, { Component } from 'react';
import { Link } from "react-router-dom";

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
            <div className="App">
                <h1>Login</h1>
                    <form onSubmit={this.sendData}>
                        <input type="email" placeholder="example@org.co" name="email"
                                value={this.state.credentials.email}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input type="password" placeholder="Password" name="password"
                                value={this.state.credentials.password}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input type='submit' value='Login' />
                    </form>
                {this.state.errors && <p style={{ color: "red" }}>Invalid credentials.</p>}
                <p className="text-normal">Don't have an account yet? <Link to="/register">Register!</Link></p>
                <br />
                <p>Or go to <Link to="/main">main page</Link></p>
            </div>
        );
    }
}

export default Login;
