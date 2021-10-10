import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import logo from "../img/logo-white.png";

const API_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/v1/users/auth/register/";

class Register extends Component {

    state = {
        credentials: {
            email: '',
            password1: '',
            password2: ''
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
                    this.setState({ credentials: {
                        email: '',
                        password: '',
                        confirmPassword: ''
                    }});
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
                <img style={{ width: '29vh', height: '25vh' }} src={logo} alt="Logo" />
                    <form onSubmit={this.sendData}>
                        <input className="input-field" type="email" placeholder="example@org.co" name="email"
                                value={this.state.credentials.email}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="password" placeholder="Password" name="password1"
                                value={this.state.credentials.password1}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="password" placeholder="Confirm password" name="password2"
                                value={this.state.credentials.password2}
                                onChange={this.inputChanged}></input>
                        <br />
                        {this.state.errors && <p style={{ color: "red" }}>Passwords do not match.</p>}
                        <input className="input-submit" type='submit' value='REGISTER' />
                    </form>
                <p class="text-normal">Already have an account? <Link to="/" className="text-link">Go back to login.</Link></p>
            </div>
        );
    }
}

export default Register;
